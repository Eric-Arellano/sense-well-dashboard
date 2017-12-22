// @flow
import * as React from 'react'

type Props = {
  children: React.Element<string>  // can only be a single child of type string
}

const Entry = ({children}: Props) => (
  <p>{children}</p>
)

export default Entry