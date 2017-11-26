// @flow
import React from 'react'
import { Row, Col } from 'reactstrap'
import { SummaryWidget, Chart } from 'components'
import type { MetricSummary } from 'flow/types'

type Props = {
  metricSummaries: Array<MetricSummary>
}

const Dashboard = (props: Props) => {
  return (
    <div className="animated fadeIn">
      <Row>
        {props.metricSummaries.map((metric, index) => (
          <Col key={index} xs="12" sm="6" lg="3">
            <SummaryWidget metricSummary={metric}/>
          </Col>
        ))}
      </Row>
      <Row>
        <Col xs={"24"} sm={"12"} lg={"6"}>
          <Chart />
        </Col>
      </Row>
    </div>
  )
}

export default Dashboard