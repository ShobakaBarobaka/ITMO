import static java.lang.Math.*;


public class ProgLab1 {
    // метод выводит получившийся двумерный массив на экран в виде матрицы
    private static void printArray(float[][] fnlArr){
        for (float[] str : fnlArr) {
            for(float elem : str) {
                System.out.format("%10.2f ", elem);
            }
            System.out.println();
        }
    }

    // метод вычисляет элементы массива по заданым формулам
    private static float[][] initArray(long[] additionalArray, float[][] finalArray, float[] randomArray){
        for(int i=0; i < finalArray.length; i ++){
            for(int j=0; j < finalArray[0].length; j++){
                long ad = additionalArray[i];
                float rnd = randomArray[j];

                if (ad == 8) {
                    finalArray[i][j] = (float) (sin(pow(pow((1 / (4 * rnd)), 3),
                            asin(((rnd - 3) * E / 2) + 1))));
                } else if (ad == 5 || ad == 7 || ad == 10 ||
                         ad == 12 || ad == 14 || ad == 17) {
                    finalArray[i][j] = (float) (cos(pow(3, (double) 1 / 2) * (pow(E, rnd))));
                } else {
                    finalArray[i][j] = (float) (pow((1 - tan(pow((atan((rnd - 3) / 2 * E + 1)),
                            (tan(rnd) / 0.5)))) / pow(E, (sin(pow((double) 3 / 4 / rnd, 2)))), 3));
                }
            }
        }
        return finalArray;
    }

    public static void main(String[] args) {
        long[] z = new long[13]; // создаем массив размера 13
        for(int i = 0; i < z.length; i++){
            z[i] = i + 5; // заполняем массив числами от 5 до 17
        }
        float[] x = new float[18];
        for(int i = 0; i < x.length; i++){
            x[i] = (float)(Math.random() * 20.0 - 13.0); // заполняем массив случайными числами от -13 до 7
        }
        float[][] z1 = new float[13][18]; // создаём двумерный массив 13х18
        printArray(initArray(z,z1,x));

    }
}
