import React, { Component } from 'react';
import MetricSummary2 from "../../components/Widgets/MetricSummary2";

class Dashboard extends Component {

  render() {
    return (
      <div className="animated fadeIn">
        Hello World
        <MetricSummary2 currentValue={43} average={74} threshold={23} />
      </div>
    )
  }
}

export default Dashboard;
