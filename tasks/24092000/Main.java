public class Main {
	public static void main(String[] args) {
		short[] f = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18};
		
		float[] x = new float[10];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 18.0 - 9.0);
				
		double[][] e = new double[17][10];
		for (int i = 0; i < e.length; i++) {
			for (int j = 0; j < e[i].length; j++) {
				switch ((int) f[i]) {
					case 12:
						e[i][j] = Math.tan(Math.log(Math.pow(Math.sin(x[j]), 2)));
						break;
					case 2:
					case 3:
					case 5:
					case 6:
					case 7:
					case 8:
					case 13:
					case 15:
						e[i][j] = Math.pow((2*Math.pow((Math.log(Math.abs(x[j]))), (Math.cbrt(x[j])))), (Math.log(Math.pow(Math.sin(x[j]), 2))));
						break;
					default:
						e[i][j] = Math.pow((Math.PI*Math.pow((Math.cos(x[j])), (Math.tan(x[j])+1))), (3/(Math.tan(x[j]/(x[j]+4))-2/3)));
						break;
				}
				System.out.printf("%.3f ", e[i][j]);
			}
			System.out.println();
		}
	}
}
