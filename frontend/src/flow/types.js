// @flow

export type MetricSummary = {
  name: string,
  unit: string,
  currentValue: number,
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