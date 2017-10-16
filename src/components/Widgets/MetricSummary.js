// @flow
import React from 'react';
import classNames from 'classnames';
import {mapToCssModules} from 'reactstrap/lib/utils';

type Props = {
  className: string,
  cssModule: any,
  name: string,
  currentValue: number,
  date: Date,
  average: number,
  threshold: (number) => boolean,
  thresholdText: string
};

const MetricSummary = (props: Props) => {
  const {className, cssModule, name, currentValue, date, average, threshold, thresholdText, ...attributes} = props;
  const okay = threshold(currentValue) ? 'okay' : 'bad';
  const daysDiff = Math.round((new Date() - date)/(1000*60*60*24));
  const classes = mapToCssModules(classNames("metric-box", className, okay), cssModule);

  return (
    <div>
      <div className={classes}>
        <span className={"mainText"}>{currentValue}</span>
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
        <span>Last updated {daysDiff} days ago.</span>
      </div>
      <h3>{name}</h3>
    </div>
  )
};

export default MetricSummary;