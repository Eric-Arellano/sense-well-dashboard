// @flow

export type Metric = {
  name: string,
  unit: string,
  currentValue: number,
  datapoints: Timeseries,
  date: Date,
  average: number,
  threshold: (number) => boolean,
  thresholdText: string
}

export type Community = {
  name: string,
  latitude: number,
  longitude: number,
  size: number,
  installation: Date,
  lastInspection: Date
}

export type Timeseries = Array<[string, number]>