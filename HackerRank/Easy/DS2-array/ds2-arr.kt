import java.io.*
import java.math.*
import java.security.*
import java.text.*
import java.util.*
import java.util.concurrent.*
import java.util.function.*
import java.util.regex.*
import java.util.stream.*
import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.io.*
import kotlin.jvm.*
import kotlin.jvm.functions.*
import kotlin.jvm.internal.*
import kotlin.ranges.*
import kotlin.sequences.*
import kotlin.text.*

// Complete the hourglassSum function below.
fun hourglassSum(arr: Array<Array<Int>>): Int {
	var sum: Int = 0 
	var temp: Int 

	for (i in 1..4) {
		for (j in 1..4) {
			temp = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
				if (temp > sum || (i == 1 && j == 1))
					sum = temp
		}
	}   

	return sum 
}

fun main(args: Array<String>) {
	val scan = Scanner(System.`in`)
	val arr = Array<Array<Int>>(6, { Array<Int>(6, { 0 }) })

	for (i in 0 until 6) {
		arr[i] = scan.nextLine().split(" ").map{ it.trim().toInt() }.toTypedArray()
	}

	val result = hourglassSum(arr)

	println(result)
}

