CREATE TABLE daily_conditions (
  day             DATE                                    NOT NULL,
  community_id    INT REFERENCES community (community_id) NOT NULL,
  flow_count      INT                                     NOT NULL,
  flow_sum        DOUBLE PRECISION,
  salinity_count  INT                                     NOT NULL,
  salinity_sum    DOUBLE PRECISION,
  turbidity_count INT                                     NOT NULL,
  turbidity_sum   DOUBLE PRECISION,
  PRIMARY KEY (day, community_id)
);

SELECT create_hypertable('daily_conditions', 'time');

CREATE TABLE community (
  community_id INT PRIMARY KEY,
  name         TEXT  NOT NULL,
  lat_long     POINT NOT NULL,
  size         INT,
  install_date DATE,
  update_date  DATE
);

CREATE TABLE flow (
  most_recent_daily_value DOUBLE PRECISION,
  daily_average           DOUBLE PRECISION NOT NULL
);

CREATE TABLE salinity (
  most_recent_daily_value DOUBLE PRECISION,
  daily_average           DOUBLE PRECISION NOT NULL
);

CREATE TABLE turbidity (
  most_recent_daily_value DOUBLE PRECISION,
  daily_average           DOUBLE PRECISION NOT NULL
);


