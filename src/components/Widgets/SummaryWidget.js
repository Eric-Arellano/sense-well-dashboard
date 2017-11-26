// @flow
import React from 'react';
import classNames from 'classnames';
import {mapToCssModules} from 'reactstrap/lib/utils';
import type { MetricSummary } from 'flow/types'

type Props = {
  className: string,
  cssModule: any,
  metricSummary: MetricSummary
};

const SummaryWidget = (props: Props) => {
  const {className, cssModule, metricSummary} = props
  const {name, unit, currentValue, date, average, threshold, thresholdText } = metricSummary
  const okay = threshold(currentValue) ? 'okay' : 'bad';
  const daysDiff = Math.round((new Date() - date)/(1000*60*60*24));
  const classes = mapToCssModules(classNames("metric-box", className, okay), cssModule);

  return (
    <div className={classes}>
      <div className={"widget"}>
        <div className={"mainText"}>
          <span className={"currentValue"}>{currentValue}</span>
          <span className={"unit"}>{unit}</span>
        </div>
        <ul>
          <li>
            <strong>{average}</strong>
            <span>average</span>
          </li>
          <li>
            <strong>{thresholdText}</strong>
            <span>safe values</span>
          </li>
        </ul>
        <div className={"lastUpdatedBox"}>
          <span className={"date"}>Last updated {daysDiff} days ago.</span>
        </div>
      </div>
      <h3 className={"metricName"}>{name}</h3>
    </div>
  )
};

export default SummaryWidget;