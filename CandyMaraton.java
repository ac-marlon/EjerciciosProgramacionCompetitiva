package candymaraton;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

public class CandyMaraton {

    public static void main(String[] args) {

        String input;
        String fila;
        int resultado = 0;
        int m, n;
        ArrayList listaResultados = new ArrayList();
        System.out.println("INPUT");

        do {
            Scanner s = new Scanner(System.in);
            input = s.nextLine();
            StringTokenizer st = new StringTokenizer(input);
            ArrayList arreglotemp;
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            int[][] matriz = new int[m][n];

            for (int i = 0; i < m; i++) {
                fila = s.nextLine();
                arreglotemp = procesarCadena(fila);
                for (int j = 0; j < n; j++) {
                    matriz[i][j] = (int) arreglotemp.get(j);
                }
            }
            listaResultados.add(saberMayor(matriz, m, n, resultado));
        } while (n != 0 && m != 0);
        System.out.println(" ");
        System.out.println("OUTPUT");
        for (int i = 0; i < (listaResultados.size() - 1); i++) {
            System.out.println(listaResultados.get(i));
        }
    }

    public static ArrayList procesarCadena(String numeros) {
        ArrayList arregloCadenas = new ArrayList();
        StringTokenizer st = new StringTokenizer(numeros);
        while (st.hasMoreTokens()) {
            arregloCadenas.add(Integer.parseInt(st.nextToken()));
        }
        return arregloCadenas;
    }

    public static int saberMayor(int[][] matriz, int m, int n, int resultado) {
        int auxMayor = 0;
        int fil = 0, col = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matriz[i][j] > auxMayor) {
                    auxMayor = matriz[i][j];
                    fil = i;
                    col = j;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                matriz[fil][col] = 0;
                if (col > 0) {
                    matriz[fil][col - 1] = 0;
                }
                if (col < n - 1) {
                    matriz[fil][col + 1] = 0;
                }
                if (fil > 0) {
                    matriz[fil - 1][j] = 0;
                }
                if (fil < m - 1) {
                    matriz[fil + 1][j] = 0;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
            }
        }

        boolean terminar = false;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matriz[i][j] != 0) {
                    terminar = true;
                    break;
                } else {
                    terminar = false;
                }
            }
        }

        resultado += auxMayor;
        if (terminar == true) {
            return saberMayor(matriz, n, m, resultado);
        } else {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (matriz[i][j] != 0) {
                        resultado += matriz[i][j];
                        break;
                    }
                }
            }
            return resultado;
        }
    }
}
