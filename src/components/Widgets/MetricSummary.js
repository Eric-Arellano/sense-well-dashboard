import React, {Component} from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import {mapToCssModules} from 'reactstrap/lib/utils';

// SEE WIDGET 3 for basis

const propTypes = {
  className: PropTypes.string,
  cssModule: PropTypes.object,
  name: PropTypes.string.isRequired,
  units: PropTypes.string.isRequired,
  date: PropTypes.instanceOf(Date),
  currentValue: PropTypes.number,
  average: PropTypes.number,
  threshold: PropTypes.number
};

const defaultProps = {

};

class MetricSummary extends Component {
  render() {
    const {className, cssModule, name, units, date, currentValue, average, threshold,
      ...attributes} = this.props;

    const okay = currentValue > threshold ? "okay" : "bad";

    // const classes = mapToCssModules(classNames("social-box", className, okay), cssModule);

    return (
      /*<div className={classes}>*/
    <div >
        <ul>
          <li>
            <strong>{average}</strong>
            <span>average</span>
          </li>
          <li>
            <strong>{vals[2]}</strong>
            <span>threshold</span>
          </li>
        </ul>
      </div>
    )
  }
}

Widget03.propTypes = propTypes;
Widget03.defaultProps = defaultProps;

export default MetricSummary;


// example call of Widget3:
// <Widget03 dataBox={() => ({variant: "facebook", friends : "89k", feeds: "459"})}/>