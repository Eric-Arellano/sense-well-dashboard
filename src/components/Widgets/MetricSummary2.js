import React, {Component} from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import {mapToCssModules} from 'reactstrap/lib/utils';

const propTypes = {
  className: PropTypes.string,
  cssModule: PropTypes.object,
  variant2: PropTypes.string,
  average: PropTypes.number,
  threshold: PropTypes.number  // TODO: make this a boolean function
};

const defaultProps = {

};

class MetricSummary2 extends Component {
  render() {
    const {className, cssModule, variant2, average, threshold, ...attributes} = this.props;

    if (!variant2 || ['facebook', 'twitter', 'linkedin', 'google-plus'].indexOf(variant2) < 0) {
      return ( null );
    }

    const icon = "fa fa-" + variant2;

    const classes = mapToCssModules(classNames("social-box", className, variant2), cssModule);

    return (
      <div className={classes}>
        <i className={icon}></i>
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

MetricSummary2.propTypes = propTypes;
MetricSummary2.defaultProps = defaultProps;

export default MetricSummary2;