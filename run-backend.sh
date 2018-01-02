#!/usr/bin/env bash
# usage:
#   run: `./run-backend.sh`
#   types: `./run-backend.sh types`
#   tests: `./run-backend.sh tests`
#   coverage: `./run-backend.sh coverage`

if [ $# -gt 0 ]
then
  flag=$1
fi;

main() {
  source backend/bin/activate
  if [ "$flag" == "test" ]
  then
    test_backend
  elif [ "$flag" == "types" ]
  then
    check_backend_types
  elif [ "$flag" == "coverage" ]
  then
    check_test_coverage
  else
    run_backend
  fi
}

run_backend() {
  export FLASK_APP=backend/src/app.py
  flask run
}

test_backend() {
  cd backend/
  python -m unittest
  cd ../
}

check_backend_types() {
  cd backend/
  mypy --strict-optional --package src
  cd ../
}

check_test_coverage() {
  cd backend/
  mypy --strict-optional --package src
  cd ../
}

main "$@"