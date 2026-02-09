import { Box, Button, Typography, Link } from '@mui/material'
import AuthLayout from "../components/layout/AuthLayout";
import started from "../assets/started.png"
import logo from "../assets/logo.png"
export default function GetStarted() {
  return (
    <AuthLayout>
      {/* Columna izquierda */}
      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          bgcolor: '#FFF',
        }}
      >
        <Box
          component="img"
          src={started}   // pon aquí tu imagen
          alt="Calendar illustration"
          sx={{
            maxWidth: '85%',
            height: 'auto',
          }}
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
        {/* Logo */}
        <Box
          component="img"
          src={logo}// tu logo
          alt="Suntsy logo"
          sx={{ width: 144, mb: 3 }}
        />

        <Typography variant="h4" sx={{ mb: 2 }}>
          Let’s get started
        </Typography>

        <Typography color='#0000000' sx={{ mb: 4 }}>
          Save your favorite sky photos, share them with friends, and relive
          your memories through Suntsy, your personal sky tracker calendar.
        </Typography>

        <Button
          variant="contained"
          sx={{
            bgcolor: '#D59A9A',
            color: '#ffffff',
            mb: 2,
            py: 1.2,
            borderRadius: 2,
            boxShadow: 'none',
            textTransform: 'none',
            '&:hover': {
              bgcolor: '#C48888',
              boxShadow: 'none',
            },
          }}
        >
          Get started
        </Button>

        <Typography variant="body2" color="text.secondary">
          Already have an account?{' '}
          <Link href="/login" underline="hover">
            Log in
          </Link>
        </Typography>
      </Box>
    </AuthLayout>
  )
}
