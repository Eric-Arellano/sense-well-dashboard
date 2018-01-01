CREATE TABLE daily_conditions (
  date            DATE                                  NOT NULL,
  location_id     INT REFERENCES location (location_id) NOT NULL,
  flow_count      INT                                   NOT NULL,
  flow_sum        DOUBLE PRECISION                      NOT NULL,
  salinity_count  INT                                   NOT NULL,
  salinity_sum    DOUBLE PRECISION                      NOT NULL,
  turbidity_count INT                                   NOT NULL,
  turbidity_sum   DOUBLE PRECISION                      NOT NULL,
  PRIMARY KEY (date, location_id)
);

SELECT create_hypertable('daily_conditions', 'time');

CREATE TABLE location (
  location_id  INT PRIMARY KEY,
  name         TEXT  NOT NULL,
  lat_long     POINT NOT NULL,
  size         INT,
  install_date DATE,
  update_date  DATE
);

