import { createTheme } from '@mui/material/styles'

const theme = createTheme({
  palette: {
    background: {
      default: '#F6F3F3',
      paper: '#FFFFFF',
    },
    text: {
      primary: '#1A1A1A',
      secondary: '#6B6B6B',
    },
  },

  typography: {
    fontFamily: 'Poppins, system-ui, sans-serif',

    h4: {
      fontWeight: 600, // Semibold
    },

    body1: {
      fontWeight: 400, // Regular
    },

    body2: {
      fontWeight: 300, // Light
    },

    button: {
      fontWeight: 500, // Medium
      textTransform: 'none',
    },
  },

  shape: {
    borderRadius: 12,
  },

  components: {
    MuiButton: {
      variants: [
        {
          props: {variant: 'suntsy'},
          style: {
            backgroundColor: '#D59A9A',
            color: '#FFFFFF',
            height: 44,
            borderRadius: 6,
            paddingInline: 24,
            boxShadow: 'none',

            '&:hover': {
              backgroundColor: '#C48888',
              boxShadow: 'none',
            },
          },
        },
      ],
    },
  },
})

export default theme
