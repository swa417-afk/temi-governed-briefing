package edu.uky.havoc.clinical

import com.google.gson.Gson
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import java.io.IOException

class ClinicalApiClient(
  private val baseUrl: String,
  private val http: OkHttpClient = OkHttpClient(),
  private val gson: Gson = Gson()
) {
  private val jsonType = "application/json".toMediaType()

  @Throws(IOException::class)
  fun getPatientBrief(req: BriefingRequest): PatientBriefResponse {
    val body = gson.toJson(req).toRequestBody(jsonType)
    val httpReq = Request.Builder()
      .url("$baseUrl/api/briefings/patient")
      .post(body)
      .build()

    http.newCall(httpReq).execute().use { resp ->
      if (!resp.isSuccessful) throw IOException("Brief failed: HTTP ${resp.code}")
      return gson.fromJson(resp.body!!.string(), PatientBriefResponse::class.java)
    }
  }

  @Throws(IOException::class)
  fun sendStaffSnapshot(req: StaffSnapshotRequest): String {
    val body = gson.toJson(req).toRequestBody(jsonType)
    val httpReq = Request.Builder()
      .url("$baseUrl/api/staff/snapshot")
      .post(body)
      .build()

    http.newCall(httpReq).execute().use { resp ->
      if (!resp.isSuccessful) throw IOException("Snapshot failed: HTTP ${resp.code}")
      return resp.body?.string() ?: "{}"
    }
  }

  @Throws(IOException::class)
  fun logUrinaryStatus(req: UrinaryStatusRequest): String {
    val body = gson.toJson(req).toRequestBody(jsonType)
    val httpReq = Request.Builder()
      .url("$baseUrl/api/urination/log")
      .post(body)
      .build()

    http.newCall(httpReq).execute().use { resp ->
      if (!resp.isSuccessful) throw IOException("Urinary log failed: HTTP ${resp.code}")
      return resp.body?.string() ?: "{}"
    }
  }
}
