// @flow
import React from 'react';
import type { MetricSummary } from 'flow/types'
import s from './Widget.module.css'

type Props = {
  metricSummary: MetricSummary
};

const Widget = (props: Props) => {
  const {name, unit, currentValue, date, average, threshold, thresholdText } = props.metricSummary
  const okay = threshold(currentValue) ? 'okayMainText' : 'badMainText';
  const daysDiff = Math.round((new Date() - date)/(1000*60*60*24));
  return (
    <div className={s.container}>
      <div className={s.box}>
        <div className={s[okay]}>
          <span className={s.currentValue}>{currentValue}</span>
          <span className={s.unit}>{unit}</span>
        </div>
        <ul className={s.bottom}>
          <li className={s.average}>
            <strong>{average}</strong>
            <span>average</span>
          </li>
          <li>
            <strong>{thresholdText}</strong>
            <span>safe values</span>
          </li>
        </ul>
        <div className={s.lastUpdated}>
          <span>Last updated {daysDiff} days ago.</span>
        </div>
      </div>
      <h3 className={s.metricName}>{name}</h3>
    </div>
  )
};

export default Widget;