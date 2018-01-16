# Database instructions

## To install TimeScaleDB
1. [Follow TimeScale's documentation](http://docs.timescale.com/v0.8/getting-started/installation/mac/installation-homebrew)
1. `CREATE DATABASE sensewell`
1. `\c sensewell`
1. `CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;`

## To access PSQL
1. `psql -U postgres -h localhost -d sensewell`