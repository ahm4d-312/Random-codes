using System;
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("fuck this shit");
        int a = 2, b = 1;
        Console.Write((a > b ? "a>b" : "a<b"));
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