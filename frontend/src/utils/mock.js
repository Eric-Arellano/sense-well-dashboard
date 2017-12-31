// @flow
import type { Community, Metric } from 'flow/types'

export const mockCommunity = (): Community => {
  return {
    name: 'Wusuta Sakakyere',
    latitude: 49.4814,
    longitude: 39.1391,
    size: 431,
    installation: new Date(2010, 5, 14),
    lastInspection: new Date(2017, 11, 11)
  }
}

export const mockMetrics = (): Array<Metric> => {

  const widget1: Metric = {
    name: 'Water flow',
    unit: 'L/hr',
    date: new Date(2017, 4, 11),
    datapoints: data,
    currentValue: 43,
    average: 73,
    threshold: (value) => value > 20,
    thresholdText: '> 20'
  }

  const widget2: Metric = {
    name: 'Turbidity',
    unit: '%',
    date: new Date(2017, 8, 17),
    datapoints: data,
    currentValue: 65,
    average: 32,
    threshold: (value) => value < 33,
    thresholdText: '< 33%'
  }

  const widget3: Metric = {
    name: 'Salinity',
    unit: 'μS/cm',
    date: new Date(2017, 9, 14),
    currentValue: 0.41,
    datapoints: data,
    average: 0.84,
    threshold: (value) => value < 0.6,
    thresholdText: '< 0.6'
  }

  return [widget1, widget2, widget3]
}

const data = [
  ['2017-01-24 00:00', 0.01],
  ['2017-01-24 01:00', 0.13],
  ['2017-01-24 02:00', 0.07],
  ['2017-01-24 03:00', 0.04],
  ['2017-01-24 04:00', 0.33],
  ['2017-01-24 05:00', 0.2],
  ['2017-01-24 06:00', 0.08],
  ['2017-01-24 07:00', 0.54],
  ['2017-01-24 08:00', 0.95],
  ['2017-01-24 09:00', 1.12],
  ['2017-01-24 10:00', 0.66],
  ['2017-01-24 11:00', 0.06],
  ['2017-01-24 12:00', 0.3],
  ['2017-01-24 13:00', 0.05],
  ['2017-01-24 14:00', 0.5],
  ['2017-01-24 15:00', 0.24],
  ['2017-01-24 16:00', 0.02],
  ['2017-01-24 17:00', 0.98],
  ['2017-01-24 18:00', 0.46],
  ['2017-01-24 19:00', 0.8],
  ['2017-01-24 20:00', 0.39],
  ['2017-01-24 21:00', 0.4],
  ['2017-01-24 22:00', 0.39],
  ['2017-01-24 23:00', 0.28]
]
