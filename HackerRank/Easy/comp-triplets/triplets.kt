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

// Complete the compareTriplets function below.
fun compareTriplets(a: Array<Int>, b: Array<Int>): Array<Int> {
	var alice: Int = 0
	var bob: Int = 0
	var c : Array<Int> = arrayOf(0,0)

	for(i in 0..2){
		var sub : Int = a[i] - b[i]
		
		if (sub > 0)
			alice++
		else if (sub < 0)
			bob++
	}

	c.set(0, alice)
	c.set(1, bob)

	return c
}

fun main(args: Array<String>) {
    val a = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()
    val b = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

	val result = compareTriplets(a, b)
	println(result.joinToString(" "))
}

