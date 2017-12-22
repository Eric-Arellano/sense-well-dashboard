// @flow
import * as React from 'react'
import s from './Button.module.css'

type ButtonType = 'success' | 'danger'

type Props = {
  children: React.Element<string>,
  handleClick: () => mixed,
  type?: ButtonType,
  disabled?: boolean
}

const Button = ({children, handleClick, type, disabled}: Props) => (
  <button onClick={handleClick}
          className={s[type]}
          disabled={disabled}>
    {children}
  </button>
)

Button.defaultProps = {
  children: '',
  type: 'danger',
  disabled: false
}

export default Button