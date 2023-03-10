#!/usr/bin/env python3
#
# JSON textfile based database to store test data
# JSON document can be inserted into the database and queries can be performed:
# - query a value
# - simple boolean check of data in the database (comparing two measures, check that one measure is greater than
#   a given threshold.
#
# data is grouped by session, for each operation, a session id can be provided, if it is not the case
# the last created session will be used (a new session will be created if store is empty).
#
# a session can be explicitely created and the session id will be returned. this id can be used
# for subsequent operations.
#
# tdb reset
# tdb new-session
#   <id-session>
# tdb list-sessions
# tdb <op> [--session=<id-session>] <data>
#
# By Hector Cao (hector.cao@canonical.com)

import os
import sys
import json
import filelock
import subprocess
import uuid
import shutil
from tinydb import TinyDB, Query, where

class AttrDict(dict):
    """ Dictionary subclass whose entries can be accessed by attributes (as well
        as normally).

    >>> obj = AttrDict()
    >>> obj['test'] = 'hi'
    >>> print obj.test
    hi
    >>> del obj.test
    >>> obj.test = 'bye'
    >>> print obj['test']
    bye
    >>> print len(obj)
    1
    >>> obj.clear()
    >>> print len(obj)
    0
    """
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    @classmethod
    def from_nested_dicts(cls, data):
        """ Construct nested AttrDicts from nested dictionaries. """
        if not isinstance(data, dict):
            return data
        else:
            return cls({key: cls.from_nested_dicts(data[key]) for key in data})

class SessionDB:
    def __init__(self, session_id, fname):
        self.db = TinyDB(fname, sort_keys=True, indent=2, separators=(',', ': '))
        self.session_id = session_id

    def __del__(self):
        self.db.close()

    def run(self, method, args) -> int:
        if method == 'insert':
            data = None
            # data is given at stdin (with pipe)
            if not sys.stdin.isatty():
                data = sys.stdin.read()
            else:
                try:
                    data = ' '.join(args)
                except:
                    data = None
                    pass
            if data is not None and len(data)>0:
                json_dict = json.loads(data)
                self.db.insert(json_dict)

        if method == 'get':
            q = Query()
            req_str = ' '.join(args)
            val = eval(f'self.db.get(q.{req_str})')
            attr_dict = AttrDict.from_nested_dicts(val)
            val = eval(f'attr_dict.{req_str}')
            print(val)

        if method == 'test':
            q = Query()
            expr = args[0]
            val=eval(f'self.db.get(q.{expr})')
            if val is None or len(val) == 0:
                return 1

        if method == 'check':
            q = Query()
            expr = args[0]
            expr_arr = expr.split(' ')
            left_operand = expr_arr[0]
            op = expr_arr[1]
            right_operand = expr_arr[2]

            # evaluate left operand
            try:
                val1 = eval(f'self.db.get(q.{left_operand})')
                attr_dict1 = AttrDict.from_nested_dicts(val1)
                val1 = eval(f'attr_dict1.{left_operand}')
            except:
                val1 = left_operand

            # evaluate right operand
            try:
                val2 = eval(f'self.db.get(q.{right_operand})')
                attr_dict2 = AttrDict.from_nested_dicts(val2)
                val2 = eval(f'attr_dict2.{right_operand}')
            except:
                val2 = right_operand

            expr = f'{val1} {op} {val2}'
            try:
                val = eval(expr)
            except NameError as e:
                print(e)
                return 1
            print(f'Checking: {expr} against the database -> {val}')
            if not val:
                return 1
        return 0

class TestDB:

    def __init__(self, ffolder='/tmp/tdb-0c72d5e0-be86-11ed-afa1-0242ac120002/'):
        self.ffolder = ffolder
        self.db_manifest = TinyDB(f'{ffolder}/manifest.json', sort_keys=True, indent=2, separators=(',', ': '))

        self.sessions = []
        for s in self.list_sessions():
            fname = f'{ffolder}/tdb-{s}.json'
            self.sessions.append(SessionDB(s, fname))

    def __del__(self):
        self.db_manifest.close()

    # return last created session if session_id not found or None
    def get_active_session(self, session_id):
        session = self.get_session(session_id)
        if session is not None:
            return session
        self.sessions[0]

    def get_session(self, session_id):
        for s in self.sessions:
            if session_id == s.session_id:
                return s
        return None

    # returned session_id can be:
    # - the session_id given in parameter if it exists
    # - a brand new session created if session_id=None or session_id cannot be found
    # - last created session id if session_id=None
    def new_session(self, session_id=None, use_last_created=False):
        if self.get_session(session_id) is not None:
            return session_id

        sessions = self.db_manifest.get(Query().sessions)
        if sessions is None:
            sessions = []
        else:
            sessions = sessions.get("sessions")

        if len(sessions) > 0:
            if session_id in sessions:
                return session_id
            if use_last_created and session_id is None:
                return sessions[-1]

        if session_id is None:
            session_id = str(uuid.uuid4())

        sessions.append(session_id)
        self.db_manifest.upsert({"sessions": sessions}, Query().sessions.exists())
        fname = f'{self.ffolder}/tdb-{session_id}.json'
        self.sessions.append(SessionDB(session_id, fname))

        return session_id        
        
    def list_sessions(self) -> [str]:
        sessions = self.db_manifest.get(Query().sessions)
        if sessions is None:
            return []
        s = sessions.get("sessions")
        return s

    def run(self, session_id, method, args):
        session_id = self.new_session(session_id, use_last_created=True)
        session = self.get_session(session_id)

        return session.run(method, args)

def tdb(ffolder, args):
    import argparse
    method = args[0]
    parser = argparse.ArgumentParser()
    parser.add_argument('--session-id', nargs='?')
    parse_args, unknown_args = parser.parse_known_args(args[1:])

    if method == 'reset':
        try:
            shutil.rmtree(ffolder, ignore_errors=True)
        except OSError:
            pass
        return 0

    tdb = TestDB()

    if method == 'new-session':
        print(tdb.new_session(parse_args.session_id))
        return 0

    if method == 'list-sessions':
        print(tdb.list_sessions())
        return 0

    return tdb.run(parse_args.session_id, method, unknown_args)

def tdb_run(args):
    ret = 0
    ffolder = '/tmp/tdb-0c72d5e0-be86-11ed-afa1-0242ac120002/'

    # create db folder
    if not os.path.isdir(ffolder):
        os.makedirs(ffolder)
        # allow all users to access the database
        subprocess.check_call(f'setfacl -Rm other:rwX {ffolder}', shell=True)
        subprocess.check_call(f'setfacl -Rdm other:rwX {ffolder}', shell=True)

    method = args[0]
    with filelock.FileLock(f'{ffolder}/db.lock'):
        if method != 'wait':
            ret = tdb(ffolder, args)

    return ret

del Query.test
del Query.any
del Query.all
del Query.matches

if __name__ == "__main__":
    sys.exit(tdb_run(sys.argv[1:]))

