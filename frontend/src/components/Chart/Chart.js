// @flow
import React from 'react'
import { BarChart, ChartContainer, ChartRow, Charts, Resizable, styler, YAxis } from 'react-timeseries-charts'
import { Index, TimeSeries } from 'pondjs'
import type { Timeseries } from 'flow/types'

type Props = {
  label: string,
  datapoints: Timeseries
}

const style = styler([
  {key: 'value', color: 'steelblue'}
])

const parseSeries = (datapoints: Timeseries): TimeSeries => (
  new TimeSeries({
    name: 'series',
    columns: ['index', 'value'],
    points: datapoints.map(([d, value]) => [
      Index.getIndexString('1h', new Date(d)),
      value
    ])
  })
)

const Chart = ({label, datapoints}: Props) => {
  const series = parseSeries(datapoints)
  return (
    <Resizable>
      <ChartContainer timeRange={series.range()} format="%b '%y">
        <ChartRow height="150">
          <YAxis
            id="value"
            label={label}
            min={series.min('value')} max={series.max('value')}
            width="60"
            type={'linear'}
          />
          <Charts>
            <BarChart axis="value" series={series} columns={['value']} spacing={1} style={style} />
          </Charts>
        </ChartRow>
      </ChartContainer>
    </Resizable>
  )
}

export default Chart
