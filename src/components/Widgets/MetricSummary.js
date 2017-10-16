// @flow
import React from 'react';
import classNames from 'classnames';
import {mapToCssModules} from 'reactstrap/lib/utils';
import {Card, CardBody, CardFooter} from 'reactstrap';

type Props = {
  className: string,
  cssModule: any,
  currentValue: number,
  average: number,
  threshold: (number) => boolean,
  thresholdText: string
};

const MetricSummary = (props: Props) => {
  const {className, cssModule, currentValue, average, threshold, thresholdText, ...attributes} = props;
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
          <strong>{thresholdText}</strong>
          <span>safe values</span>
        </li>
      </ul>
    </div>
  )
};

export default MetricSummary;