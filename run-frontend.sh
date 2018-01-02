#!/usr/bin/env bash
# usage:
#   run: `./run-frontend.sh`
#   types: `./run-frontend.sh types`
#   build: `./run-frontend.sh build`

if [ $# -gt 0 ]
then
  flag=$1
fi;

main() {
  if [ "$flag" == "types" ]
  then
    check_frontend_types
  elif [ "$flag" == "build" ]
  then
    build_app
  else
    run_frontend
  fi
}

run_frontend() {
  cd frontend/
  yarn start
  cd ../
}

check_frontend_types() {
  cd frontend/
  yarn flow
  cd ../
}

build_app() {
  cd frontend/
  yarn build
  cd ../
}

main "$@"