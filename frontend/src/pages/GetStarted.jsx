import { Box, Button, Typography, Link } from '@mui/material'
import { Link as RouterLink } from 'react-router-dom'
import AuthLayout from '../components/layout/AuthLayout'
import started from '../assets/started.png'
import logo from '../assets/logo.png'

export default function GetStarted() {
  return (
    <AuthLayout>
      {/* Columna izquierda */}
      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          bgcolor: 'background.paper',
        }}
      >
        <Box
          component="img"
          src={started}
          alt="Calendar illustration"
          sx={{ maxWidth: '85%' }}
        />
      </Box>

      {/* Columna derecha */}
      <Box
        sx={{
          p: { xs: 4, md: 6 },
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
        }}
      >
        <Box
          component="img"
          src={logo}
          alt="Suntsy logo"
          sx={{ width: 144, mb: 3 }}
        />

        <Typography variant="h4" sx={{ mb: 2 }}>
          Let’s get started
        </Typography>

        <Typography color="text.secondary" sx={{ mb: 4, maxWidth: 420 }}>
          Save your favorite sky photos, share them with friends, and relive
          your memories through Suntsy, your personal sky tracker calendar.
        </Typography>

        {/* BOTÓN CORRECTO */}
        <Button
          variant="suntsy"
          component={RouterLink}
          to="/signup"
          sx={{
            mb: 2,
            fontSize: '20px', // Figma
          }}
        >
          Get started
        </Button>

        <Typography variant="body2" color="text.secondary">
          Already have an account?{' '}
          <Link component={RouterLink} to="/login" underline="hover">
            Log in
          </Link>
        </Typography>
      </Box>
    </AuthLayout>
  )
}