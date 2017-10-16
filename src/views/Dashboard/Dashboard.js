import React, { Component } from 'react';
import MetricSummary from "../../components/Widgets/MetricSummary";

class Dashboard extends Component {

  render() {
    return (
      <div className="animated fadeIn">
        Hello World
        <MetricSummary currentValue={43} average={74} threshold={(value) => value > 20} thresholdText={"> 20"} />
      </div>
    )
  }
}

export default Dashboard;
