import React, { Component } from 'react';
import {Row, Col} from 'reactstrap';
import MetricSummary from "../../components/Widgets/MetricSummary";

class Dashboard extends Component {

  render() {
    return (
      <div className="animated fadeIn">
        <Row>
          <Col xs="12" sm="6" lg="3">
            <MetricSummary name="Water flow" date={new Date(2017, 4, 11)} currentValue={43} average={74}
                           threshold={(value) => value > 20} thresholdText={"> 20"} />
          </Col>
          <Col xs="12" sm="6" lg="3">
            <MetricSummary name="Turbidity" date={new Date(2017, 8, 17)} currentValue={65} average={32}
                           threshold={(value) => value < 33} thresholdText={"< 33%"} />
          </Col>
          <Col xs="12" sm="6" lg="3">
            <MetricSummary name="Salinity" date={new Date(2017, 9, 14)} currentValue={0.41} average={0.84}
                           threshold={(value) => value < 0.6} thresholdText={"< 0.6"} />
          </Col>
        </Row>
      </div>
    )
  }
}

export default Dashboard;
