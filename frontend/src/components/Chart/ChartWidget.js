// @flow
import * as React from 'react'
import { Chart } from 'components'
import s from './ChartWidget.module.css'

type Props = {
  header: string
}

const Panel = ({header}: Props) => (
  <div className={s.container}>
    <h3 className={s.header}>{header}</h3>
    <div className={s.body}>
      <Chart />
    </div>
  </div>
)

export default Panel