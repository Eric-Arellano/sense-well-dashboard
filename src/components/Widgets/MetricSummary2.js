// @flow
import React, {Component} from 'react';
import classNames from 'classnames';
import {mapToCssModules} from 'reactstrap/lib/utils';

type Props = {
  className: string,
  cssModule: any,
  currentValue: number,
  average: number,
  threshold: (number) => boolean
};

const MetricSummary3 = (props: Props) => {
  const {className, cssModule, currentValue, average, threshold, ...attributes} = props;
  const okay = threshold(currentValue) ? 'okay' : 'bad';
  const classes = mapToCssModules(classNames("metric-box", className, okay), cssModule);

  return (
    <div className={classes}>
      <span className={"mainText"}>{currentValue}</span>
      <ul>
        <li>
          <strong>{average}</strong>
          <span>average</span>
        </li>
        <li>
          <strong>{threshold}</strong>
          <span>threshold</span>
        </li>
      </ul>
    </div>
  )
};

export default MetricSummary3;