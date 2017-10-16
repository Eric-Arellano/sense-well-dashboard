// @flow
import React, {Component} from 'react';
import classNames from 'classnames';
import {mapToCssModules} from 'reactstrap/lib/utils';

type Props = {
  className: string,
  cssModule: any,
  currentValue: number,
  average: number,
  threshold: number  // TODO: make this a boolean function
};

const defaultProps = {

};

class MetricSummary2 extends Component<Props> {
  render() {
    const {className, cssModule, currentValue, average, threshold, ...attributes} = this.props;

    const okay = currentValue > threshold ? 'okay' : 'bad';

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
  }
}

export default MetricSummary2;