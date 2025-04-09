"use client"

import React from 'react'
import {QueryClient, QueryClientProvider} from "@tanstack/react-query"

const queryClient = new QueryClient()

type Children = {
    children: React.ReactNode
}

const QueryProvider = ({children}:Children) => {
  return (
    <QueryClientProvider client={queryClient}>
        {children}
    </QueryClientProvider>
  )
}

export default QueryProvider