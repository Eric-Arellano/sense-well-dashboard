// @flow
import * as React from 'react'
import s from './Panel.module.css'

type Props = {
  children: React.Node,  // can be any valid react element, e.g. array of Entry
  header: string
}

const Panel = (props: Props) => {
  const {children, header} = props
  return (
    <div className={s.container}>
      <h3 className={s.header}>{header}</h3>
      <div className={s.body}>{children}</div>
    </div>
  )
}

export default Panel