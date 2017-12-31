// @flow
import React from 'react'
import type { MetricSummary } from 'flow/types'
import { Chart } from 'components'
import s from './Widget.module.css'

type Props = {
  metricSummary: MetricSummary
}

const Widget = ({metricSummary: {name, unit, currentValue, date, average, threshold, thresholdText}}: Props) => {
  const daysDiff = Math.round((new Date() - date) / (1000 * 60 * 60 * 24))
  return (
    <li className={s.container}>
      <header className={s.header}>
        <h3 className={s.metricName}>{name}</h3>
      </header>
      <main className={s.main}>
        <section className={s.mainStat} style={{color: threshold(currentValue) ? 'green' : 'red'}}>
          <span className={s.currentValue}>
            {currentValue}
          </span>
          <span className={s.unit}>
            {unit}
          </span>
        </section>
        <section className={s.minorStatsContainer}>
          <div className={s.minorStat}>
            <strong>{average}</strong>
            <span>{'average'}</span>
          </div>
          <div className={s.minorStat}>
            <strong>{thresholdText}</strong>
            <span>{'safe values'}</span>
          </div>
        </section>
        <section className={s.chartContainer}>
          <Chart />
        </section>
        <footer className={s.footer}>
          <span>{'Last updated '}<strong>{daysDiff}</strong>{' days ago.'}</span>
        </footer>
      </main>
    </li>
  )
}

export default Widget
