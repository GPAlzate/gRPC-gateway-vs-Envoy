# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [proto/registration.proto](#proto/registration.proto)
    - [Student](#housing.Student)
    - [StudentRequest](#housing.StudentRequest)
    - [StudentResponse](#housing.StudentResponse)
    - [Void](#housing.Void)
  
  
  
    - [Registration](#housing.Registration)
  

- [Scalar Value Types](#scalar-value-types)



<a name="proto/registration.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## proto/registration.proto



<a name="housing.Student"></a>

### Student
Represents a student with a unique id, a name, and a dorm


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [int32](#int32) |  | unique id for each student |
| name | [string](#string) |  | first and last name of a student |
| dorm | [string](#string) |  | dorm choice |






<a name="housing.StudentRequest"></a>

### StudentRequest
A request made by a client, specifiying id of a student. `changeDorm` and 
`new` are set when updating a student.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [int32](#int32) |  | Unique id student query |
| changeDorm | [bool](#bool) |  | True if the client requests to change the dorm, false to change name |
| new | [string](#string) |  | The updated value |






<a name="housing.StudentResponse"></a>

### StudentResponse
A response sent by a server, returning a student message and a boolean field
indicating a successful transaction


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| student | [Student](#housing.Student) |  | The deleted, created, or retrieved student. If response is not `ok`, id = 0, name = dorm = &#34;ERROR&#34; |
| ok | [bool](#bool) |  | True if transaction is successful, false otherwise |






<a name="housing.Void"></a>

### Void
Empty message for rpc&#39;s that require no request (clear and list)





 

 

 


<a name="housing.Registration"></a>

### Registration
Defines the services a client can use to register for housing.

RPC Methods:

     CreateStudent   -   adds a new student registration

     ReadStudent     -   returns a single student from database given an
                         id number

     UpdateStudent   -   updates either the name or dorm of a student given
                         an id number request

     DeleteStudent   -   deletes a student given an id number request

     ListStudent     -   lists all the students in the database

     ClearStudents   -   clears student registrations (not for client use)

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| CreateStudent | [Student](#housing.Student) | [StudentResponse](#housing.StudentResponse) | Creates a student from a student message. Returns created student with ok response |
| ReadStudent | [StudentRequest](#housing.StudentRequest) | [StudentResponse](#housing.StudentResponse) | Reads a student, queried by id number. Returns student with ok response |
| UpdateStudent | [StudentRequest](#housing.StudentRequest) | [StudentResponse](#housing.StudentResponse) | Updates a student&#39;s name or dorm. Specified by `changeDorm` boolean. Returns new student. |
| DeleteStudent | [StudentRequest](#housing.StudentRequest) | [StudentResponse](#housing.StudentResponse) | Deletes a registration queried by id and returns the deleted student |
| ListStudents | [Void](#housing.Void) | [StudentResponse](#housing.StudentResponse) stream | Lists all the registered students. Returns a stream of students |
| ClearStudents | [Void](#housing.Void) | [Void](#housing.Void) | Removes all registered students |

 



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

