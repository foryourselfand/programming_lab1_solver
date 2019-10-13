public class Main {
	public static void main(String[] args) {
		int[] k = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18};
		
		float[] x = new float[16];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 11.0 - 9.0);
				
		double[][] a = new double[17][16];
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[i].length; j++) {
				switch (k[i]) {
					case 12:
						a[i][j] = ((x/0.25)^(2*((x-1)/pi)^3)/2)^2;
						break;
					case 3:
					case 4:
					case 5:
					case 7:
					case 10:
					case 11:
					case 13:
					case 15:
						a[i][j] = (pi+arctan(0.1*(x-3.5)/11))/3/4;
						break;
					default:
						a[i][j] = arctan(cos(x))*(((sin(x)/(1-(0.5+x)/2/3))^2)^(1/4*(sin((2*x)^2)+0.5))+1/2);
						break;
				}
				System.out.printf("%.4f ", a[i][j]);
			}
			System.out.println();
		}
	}
}
