# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [proto/recruiter.proto](#proto/recruiter.proto)
    - [Company](#recruiter.Company)
    - [CompanyRequest](#recruiter.CompanyRequest)
    - [CompanyResponse](#recruiter.CompanyResponse)
    - [Void](#recruiter.Void)
  
  
  
    - [Recruiter](#recruiter.Recruiter)
  

- [Scalar Value Types](#scalar-value-types)



<a name="proto/recruiter.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## proto/recruiter.proto



<a name="recruiter.Company"></a>

### Company
Represents a company with a name, code, numer of job openings,
 and isBrokerage field


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| companyCode | [int32](#int32) |  | unique id for each company |
| companyName | [string](#string) |  | name of the company |
| numOpenings | [int32](#int32) |  | how many jobs are available |
| isBrokerage | [bool](#bool) |  | determines if the company is brokerage |






<a name="recruiter.CompanyRequest"></a>

### CompanyRequest
A request made by a client, specifiying id of a student. `changeDorm` and 
`new` are set when updating a student.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| companyCode | [int32](#int32) |  | unique id for each company |
| companyName | [string](#string) |  | name of the company |
| numOpenings | [int32](#int32) |  | how many jobs are available |
| isBrokerage | [bool](#bool) |  | determines if the company is brokerage |
| ok | [bool](#bool) |  | True if transaction is successful, false otherwise |






<a name="recruiter.CompanyResponse"></a>

### CompanyResponse
A response sent by a server, returning a student message and a boolean field
indicating a successful transaction


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| company | [Company](#recruiter.Company) |  | The deleted, created, or retrieved student. If response is not `ok`, id = 0, name = dorm = &#34;ERROR&#34; |
| ok | [bool](#bool) |  | True if transaction is successful, false otherwise |






<a name="recruiter.Void"></a>

### Void
Empty message for rpc&#39;s that require no request (clear and list)





 

 

 


<a name="recruiter.Recruiter"></a>

### Recruiter
Defines the services a client can use to register for housing.

RPC Methods:

     CreateCompany   -   adds a new student registration

     ReadCompany     -   returns a single student from database given an
                         id number

     UpdateCompany   -   updates either the name or dorm of a student given
                         an id number request

     DeleteCompany   -   deletes a student given an id number request

     ListCompany     -   lists all the students in the database

     ClearCompanies   -   clears student registrations (not for client use)

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| CreateCompany | [CompanyRequest](#recruiter.CompanyRequest) | [CompanyResponse](#recruiter.CompanyResponse) | Creates a company from a company message. Returns created company with ok response |
| ReadCompany | [CompanyRequest](#recruiter.CompanyRequest) | [CompanyResponse](#recruiter.CompanyResponse) | Reads a company, queried by company code. Returns company with ok response |
| UpdateCompany | [CompanyRequest](#recruiter.CompanyRequest) | [CompanyResponse](#recruiter.CompanyResponse) | Updates a student&#39;s name or dorm. Specified by `changeDorm` boolean. Returns new student. |
| DeleteCompany | [CompanyRequest](#recruiter.CompanyRequest) | [CompanyResponse](#recruiter.CompanyResponse) | Deletes a registration queried by id and returns the deleted student |
| ListCompanies | [Void](#recruiter.Void) | [CompanyResponse](#recruiter.CompanyResponse) stream | Lists all the registered companies. Returns a stream of companies |
| ClearCompanies | [Void](#recruiter.Void) | [Void](#recruiter.Void) | Removes all registered companies |

 



## Scalar Value Types

| .proto Type | Notes | C++ Type | Java Type | Python Type |
| ----------- | ----- | -------- | --------- | ----------- |
| <a name="double" /> double |  | double | double | float |
| <a name="float" /> float |  | float | float | float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long |
| <a name="bool" /> bool |  | bool | boolean | boolean |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str |

