import React from 'react';

const sidebarMinimize = () => {
  document.body.classList.toggle('sidebar-minimized')
}

const brandMinimize = () => {
  document.body.classList.toggle('brand-minimized')
}

const SidebarMinimizer = () => {
  return (
    <button className="sidebar-minimizer" type="button"
            onClick={(event) => { sidebarMinimize(); brandMinimize() }}/>
  )
}

export default SidebarMinimizer;
