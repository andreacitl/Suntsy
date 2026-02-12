import { Box, Paper } from '@mui/material'

export default function AuthFormLayout({ children }) {
  return (
    <Box
      sx={{
        minHeight: '100vh',
        bgcolor: '#D59A9A',
        display: 'grid',
        placeItems: 'center',
        p: 3,
      }}
    >
      <Paper
        elevation={0}
        sx={{
            width: '100%',
            maxWidth: 1100,
            height: 600,
            borderRadius: 4,
        }}
      >
        {children}
      </Paper>
    </Box>
  )
}
