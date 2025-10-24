using System.Buffers;
using System.Net.Mail;
using System.Reflection.Metadata.Ecma335;
namespace MyNameSpace
{
    class Program
    {
        static void Main(string[] args)
        {
            // operations();
            // control_statements_and_loops();
            //loops();
            //I_O();
            arrays();

        }
        static void arrays()
        {
            int[] arr = { 1, 2, 3, 6, 5, 4 };
            Array.Sort(arr);
            foreach (var x in arr)
            {
                Console.Write(x + " ");
            }
            Console.WriteLine();

            Array.Reverse(arr);
            foreach (var x in arr)
            {
                Console.Write(x + " ");
            }
            Console.WriteLine();

            Console.WriteLine("\n-----" + Array.IndexOf(arr, 6) + "\n------");
            foreach (var x in arr)
            {
                Console.Write(x + " ");
            }
            Console.WriteLine();

            Array.Clear(arr);
            foreach (var x in arr)
            {
                Console.Write(x + " ");
            }
            Console.WriteLine();

        }
        static void I_O()
        {
            Console.Write("Please press a key: ");
            int input = Console.Read();
            Console.WriteLine("You pressed: " + (char)input);
        }

        static void loops()
        {
            Console.WriteLine("\n------ For Loop ------");

            for (int i = 0; i < 5; i++)
            {
                Console.Write(i);
            }
            int ii = 0;
            Console.WriteLine("\n----- While Loop -----");
            while (ii < 5)
            {
                Console.Write(ii);
                ii++;
            }
            Console.WriteLine("\n---- do While Loop ----");
            ii = 0;
            do
            {
                Console.Write(ii);
                ii++;
            } while (ii < 5);


        }

        static void control_statements_and_loops()
        {
            int num = -10;
            if (num > -10)
                Console.WriteLine("more");
            else if (num < -10)
                Console.WriteLine("less");
            else
                Console.WriteLine("equal");

            int number = 3;

            switch (number)
            {
                case 1:
                    operations();
                    break;
                case 2:
                    Console.WriteLine("Two");
                    break;
                case 3:
                    Console.WriteLine("Two+One");
                    Console.WriteLine("   |\n  \\ /\nThree");
                    break;
            }

        }
        static void operations()
        {
            Console.WriteLine("fuck this shit");
            int a = 2, b = 1;
            Console.Write(a > b ? "a>b" : "a<b");
            string? name = null;
            Console.WriteLine(name?.Length);
            int? x = null;
            int? y = x ?? -1;
            Console.WriteLine("x:" + x + "\ty:" + y);
            x ??= 11;
            y ??= 112;
            Console.WriteLine(x is int);
        }
    }
}