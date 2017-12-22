import React from 'react'
import { Button } from 'components'
import s from './Error.module.css'

type Props = {
  children: React.Element<string>,
  resetState: () => void,
}

const Error = ({children, resetState}: Props) => (
  <div className={s.base}>
    <p>{children}</p>
    <Button handleClick={resetState}>Back</Button>
  </div>
)

export default Error