// Code generated by protoc-gen-go. DO NOT EDIT.
// source: proto/recruiter.proto

package recruiter

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/options"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

//*
// Empty message for rpc's that require no request (clear and list)
type Void struct {
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Void) Reset()         { *m = Void{} }
func (m *Void) String() string { return proto.CompactTextString(m) }
func (*Void) ProtoMessage()    {}
func (*Void) Descriptor() ([]byte, []int) {
	return fileDescriptor_3c1aebc5185a9997, []int{0}
}

func (m *Void) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Void.Unmarshal(m, b)
}
func (m *Void) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Void.Marshal(b, m, deterministic)
}
func (m *Void) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Void.Merge(m, src)
}
func (m *Void) XXX_Size() int {
	return xxx_messageInfo_Void.Size(m)
}
func (m *Void) XXX_DiscardUnknown() {
	xxx_messageInfo_Void.DiscardUnknown(m)
}

var xxx_messageInfo_Void proto.InternalMessageInfo

//*
// Represents a company with a name, code, numer of job openings,
//  and is_brokerage field
type Company struct {
	// unique id for each company
	CompanyCode int32 `protobuf:"varint,1,opt,name=companyCode,proto3" json:"companyCode,omitempty"`
	// name of the company
	CompanyName string `protobuf:"bytes,2,opt,name=companyName,proto3" json:"companyName,omitempty"`
	// how many jobs are available
	NumOpenings int32 `protobuf:"varint,3,opt,name=numOpenings,proto3" json:"numOpenings,omitempty"`
	// determines if the company is brokerage
	IsBrokerage          bool     `protobuf:"varint,4,opt,name=isBrokerage,proto3" json:"isBrokerage,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Company) Reset()         { *m = Company{} }
func (m *Company) String() string { return proto.CompactTextString(m) }
func (*Company) ProtoMessage()    {}
func (*Company) Descriptor() ([]byte, []int) {
	return fileDescriptor_3c1aebc5185a9997, []int{1}
}

func (m *Company) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Company.Unmarshal(m, b)
}
func (m *Company) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Company.Marshal(b, m, deterministic)
}
func (m *Company) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Company.Merge(m, src)
}
func (m *Company) XXX_Size() int {
	return xxx_messageInfo_Company.Size(m)
}
func (m *Company) XXX_DiscardUnknown() {
	xxx_messageInfo_Company.DiscardUnknown(m)
}

var xxx_messageInfo_Company proto.InternalMessageInfo

func (m *Company) GetCompanyCode() int32 {
	if m != nil {
		return m.CompanyCode
	}
	return 0
}

func (m *Company) GetCompanyName() string {
	if m != nil {
		return m.CompanyName
	}
	return ""
}

func (m *Company) GetNumOpenings() int32 {
	if m != nil {
		return m.NumOpenings
	}
	return 0
}

func (m *Company) GetIsBrokerage() bool {
	if m != nil {
		return m.IsBrokerage
	}
	return false
}

//*
// A request made by a client, specifiying id of a student. `changeDorm` and
// `new` are set when updating a student.
type CompanyRequest struct {
	// Unique id student query
	CompanyCode int32 `protobuf:"varint,1,opt,name=companyCode,proto3" json:"companyCode,omitempty"`
	// True if the client requests to change the dorm, false to change name
	ChangeName bool `protobuf:"varint,2,opt,name=changeName,proto3" json:"changeName,omitempty"`
	// The new number of openings
	NumOpenings int32 `protobuf:"varint,3,opt,name=numOpenings,proto3" json:"numOpenings,omitempty"`
	// The updated name
	NewName              string   `protobuf:"bytes,4,opt,name=newName,proto3" json:"newName,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *CompanyRequest) Reset()         { *m = CompanyRequest{} }
func (m *CompanyRequest) String() string { return proto.CompactTextString(m) }
func (*CompanyRequest) ProtoMessage()    {}
func (*CompanyRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_3c1aebc5185a9997, []int{2}
}

func (m *CompanyRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CompanyRequest.Unmarshal(m, b)
}
func (m *CompanyRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CompanyRequest.Marshal(b, m, deterministic)
}
func (m *CompanyRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CompanyRequest.Merge(m, src)
}
func (m *CompanyRequest) XXX_Size() int {
	return xxx_messageInfo_CompanyRequest.Size(m)
}
func (m *CompanyRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_CompanyRequest.DiscardUnknown(m)
}

var xxx_messageInfo_CompanyRequest proto.InternalMessageInfo

func (m *CompanyRequest) GetCompanyCode() int32 {
	if m != nil {
		return m.CompanyCode
	}
	return 0
}

func (m *CompanyRequest) GetChangeName() bool {
	if m != nil {
		return m.ChangeName
	}
	return false
}

func (m *CompanyRequest) GetNumOpenings() int32 {
	if m != nil {
		return m.NumOpenings
	}
	return 0
}

func (m *CompanyRequest) GetNewName() string {
	if m != nil {
		return m.NewName
	}
	return ""
}

//*
// A response sent by a server, returning a student message and a boolean field
// indicating a successful transaction
type CompanyResponse struct {
	//*
	// The deleted, created, or retrieved student. If response is not `ok`,
	// id = 0, name = dorm = "ERROR"
	Company *Company `protobuf:"bytes,1,opt,name=company,proto3" json:"company,omitempty"`
	// True if transaction is successful, false otherwise
	Ok                   bool     `protobuf:"varint,2,opt,name=ok,proto3" json:"ok,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *CompanyResponse) Reset()         { *m = CompanyResponse{} }
func (m *CompanyResponse) String() string { return proto.CompactTextString(m) }
func (*CompanyResponse) ProtoMessage()    {}
func (*CompanyResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_3c1aebc5185a9997, []int{3}
}

func (m *CompanyResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CompanyResponse.Unmarshal(m, b)
}
func (m *CompanyResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CompanyResponse.Marshal(b, m, deterministic)
}
func (m *CompanyResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CompanyResponse.Merge(m, src)
}
func (m *CompanyResponse) XXX_Size() int {
	return xxx_messageInfo_CompanyResponse.Size(m)
}
func (m *CompanyResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_CompanyResponse.DiscardUnknown(m)
}

var xxx_messageInfo_CompanyResponse proto.InternalMessageInfo

func (m *CompanyResponse) GetCompany() *Company {
	if m != nil {
		return m.Company
	}
	return nil
}

func (m *CompanyResponse) GetOk() bool {
	if m != nil {
		return m.Ok
	}
	return false
}

func init() {
	proto.RegisterType((*Void)(nil), "recruiter.Void")
	proto.RegisterType((*Company)(nil), "recruiter.Company")
	proto.RegisterType((*CompanyRequest)(nil), "recruiter.CompanyRequest")
	proto.RegisterType((*CompanyResponse)(nil), "recruiter.CompanyResponse")
}

func init() { proto.RegisterFile("proto/recruiter.proto", fileDescriptor_3c1aebc5185a9997) }

var fileDescriptor_3c1aebc5185a9997 = []byte{
	// 772 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xc4, 0x55, 0xc1, 0x6e, 0x23, 0x35,
	0x18, 0x96, 0x93, 0xd2, 0xb4, 0xee, 0x26, 0xad, 0x2c, 0x15, 0x65, 0x47, 0xcb, 0xea, 0x27, 0xe2,
	0x50, 0x45, 0xdb, 0x4c, 0x36, 0x4b, 0x2f, 0x95, 0x38, 0xb4, 0x49, 0x85, 0x76, 0x41, 0x54, 0x9a,
	0xee, 0x22, 0xc1, 0xcd, 0x99, 0xf9, 0x3b, 0x63, 0x3a, 0x63, 0x0f, 0xb6, 0x67, 0x43, 0x85, 0xb8,
	0x70, 0xe3, 0xb2, 0x12, 0x41, 0xe2, 0x00, 0x2f, 0x00, 0x6f, 0xc1, 0x3b, 0xf0, 0x04, 0x48, 0x70,
	0xe6, 0x15, 0x50, 0x3c, 0x99, 0x30, 0xed, 0x56, 0x55, 0x05, 0x87, 0x3d, 0x25, 0xfe, 0xfc, 0xf9,
	0xfb, 0xbf, 0xff, 0xfb, 0x1d, 0x87, 0xee, 0xe6, 0x5a, 0x59, 0xe5, 0x6b, 0x0c, 0x75, 0x21, 0x2c,
	0xea, 0x81, 0x5b, 0xb3, 0xcd, 0x15, 0xe0, 0x3d, 0x88, 0x95, 0x8a, 0x53, 0xf4, 0x79, 0x2e, 0x7c,
	0x2e, 0xa5, 0xb2, 0xdc, 0x0a, 0x25, 0x4d, 0x49, 0xf4, 0x1e, 0xb9, 0x8f, 0x70, 0x3f, 0x46, 0xb9,
	0x6f, 0x66, 0x3c, 0x8e, 0x51, 0xfb, 0x2a, 0x77, 0x8c, 0xd7, 0xd9, 0xbd, 0x75, 0xba, 0xf6, 0xa9,
	0x12, 0x51, 0xef, 0x7b, 0x42, 0x5b, 0x63, 0x95, 0xe5, 0x5c, 0x5e, 0x32, 0xa0, 0x5b, 0x61, 0xf9,
	0x75, 0xac, 0x22, 0xec, 0x12, 0x20, 0x7b, 0x6f, 0x05, 0x75, 0xa8, 0xc6, 0xf8, 0x84, 0x67, 0xd8,
	0x6d, 0x00, 0xd9, 0xdb, 0x0c, 0xea, 0xd0, 0x82, 0x21, 0x8b, 0xec, 0x34, 0x47, 0x29, 0x64, 0x6c,
	0xba, 0xcd, 0x52, 0xa3, 0x06, 0x2d, 0x18, 0xc2, 0x1c, 0x6b, 0x75, 0x81, 0x9a, 0xc7, 0xd8, 0x5d,
	0x03, 0xb2, 0xb7, 0x11, 0xd4, 0xa1, 0xde, 0x2b, 0x42, 0x3b, 0x4b, 0x4f, 0x01, 0x7e, 0x59, 0xa0,
	0xb1, 0x77, 0xb0, 0xf6, 0x90, 0xd2, 0x30, 0xe1, 0x32, 0xc6, 0x95, 0xb3, 0x8d, 0xa0, 0x86, 0xdc,
	0xc1, 0x58, 0x97, 0xb6, 0x24, 0xce, 0xdc, 0xf1, 0x35, 0xd7, 0x58, 0xb5, 0xec, 0x9d, 0xd2, 0xed,
	0x95, 0x1f, 0x93, 0x2b, 0x69, 0x90, 0x3d, 0xa2, 0xad, 0x65, 0x75, 0x67, 0x66, 0x6b, 0xc4, 0x06,
	0xff, 0x4e, 0xae, 0x22, 0x57, 0x14, 0xd6, 0xa1, 0x0d, 0x75, 0xb1, 0x34, 0xd5, 0x50, 0x17, 0xa3,
	0x5f, 0x5b, 0x74, 0x33, 0xa8, 0xe8, 0xec, 0x67, 0x42, 0xdb, 0x63, 0x8d, 0xdc, 0x62, 0x35, 0x89,
	0x1b, 0xc4, 0x3c, 0xef, 0x86, 0x02, 0x4b, 0x37, 0xbd, 0xcf, 0xe7, 0x47, 0x63, 0xd6, 0x3e, 0x2b,
	0xb2, 0x8c, 0xeb, 0xcb, 0x43, 0xb0, 0x68, 0xac, 0xb7, 0x33, 0x41, 0x13, 0x6a, 0xe1, 0x6e, 0x00,
	0x3c, 0x47, 0x63, 0x9f, 0x01, 0x6d, 0x8e, 0x86, 0x43, 0x76, 0x9f, 0x6e, 0x9f, 0xbe, 0x44, 0x3d,
	0xd3, 0xc2, 0xa2, 0x81, 0xcf, 0x4e, 0x4e, 0x9e, 0xb3, 0x75, 0xba, 0xf6, 0x53, 0x83, 0xb4, 0xbe,
	0xfd, 0xfd, 0xcf, 0x1f, 0x1a, 0x9d, 0xde, 0xa6, 0xaf, 0x31, 0x16, 0xc6, 0xa2, 0x3e, 0x24, 0x7d,
	0xf6, 0x37, 0xa1, 0x5b, 0x01, 0xf2, 0xa8, 0xf2, 0x76, 0xff, 0x26, 0x1f, 0x6e, 0x4a, 0xb7, 0x5a,
	0xfc, 0x85, 0xcc, 0x8f, 0x5e, 0x11, 0xb6, 0xbf, 0xc4, 0x41, 0x18, 0x90, 0xca, 0x82, 0x90, 0x60,
	0x13, 0x84, 0x88, 0x5b, 0x3e, 0xe5, 0x06, 0x07, 0x30, 0x76, 0x77, 0x15, 0x22, 0x4c, 0xd1, 0xa2,
	0xd7, 0xaf, 0xe8, 0x33, 0x61, 0x13, 0xf8, 0xba, 0x36, 0xf0, 0x6f, 0x20, 0x52, 0x58, 0x6a, 0xe0,
	0x57, 0xc2, 0xd8, 0x77, 0x9f, 0x3d, 0xa6, 0xcd, 0xf7, 0x87, 0x43, 0xd6, 0xa7, 0x50, 0x6b, 0x2f,
	0xc2, 0x73, 0x5e, 0xa4, 0x16, 0x66, 0x09, 0xca, 0x52, 0x54, 0xc8, 0xf8, 0x4a, 0xbf, 0x3b, 0xac,
	0xe3, 0x5f, 0x11, 0x66, 0x09, 0x6d, 0xbf, 0xc8, 0xa3, 0xda, 0x38, 0xfe, 0x63, 0xcb, 0xe0, 0xf4,
	0x3d, 0x6f, 0xd7, 0x2f, 0x9c, 0xdc, 0xd5, 0x32, 0x8b, 0x6c, 0xbf, 0x6b, 0xd0, 0xf6, 0xc4, 0x75,
	0xfa, 0x3f, 0x4b, 0xfd, 0x46, 0xe6, 0x47, 0x3f, 0x12, 0x76, 0xf0, 0x74, 0x02, 0x09, 0x2f, 0x53,
	0x99, 0x22, 0x4a, 0xa8, 0x06, 0x89, 0x11, 0x9c, 0x2b, 0x0d, 0x89, 0x2a, 0x8c, 0x90, 0xf1, 0x1b,
	0x48, 0x19, 0xfa, 0x0f, 0x7d, 0x63, 0x8b, 0x08, 0xa5, 0x35, 0x7e, 0x59, 0xf6, 0x5a, 0xea, 0x01,
	0x6d, 0x7f, 0x2c, 0x8c, 0x2d, 0xad, 0x08, 0x34, 0x6c, 0xbb, 0xd6, 0xef, 0xe2, 0xad, 0xba, 0x35,
	0x00, 0xe6, 0xaa, 0xdc, 0x63, 0xd4, 0x0f, 0x2b, 0x81, 0x21, 0x61, 0xc7, 0xb4, 0x33, 0x4e, 0x91,
	0xeb, 0x5b, 0x44, 0xaf, 0x03, 0xbd, 0x8e, 0x53, 0xda, 0xe8, 0xaf, 0xfb, 0xe1, 0xe2, 0xe8, 0xf1,
	0x5f, 0x64, 0x7e, 0xf4, 0x07, 0x61, 0x13, 0xfa, 0xc1, 0x99, 0xc8, 0xf2, 0x14, 0x21, 0xc2, 0x4c,
	0xc1, 0x38, 0x78, 0x31, 0x01, 0x9e, 0xe7, 0x2e, 0xd6, 0x55, 0x49, 0x48, 0x84, 0x16, 0x32, 0x06,
	0x25, 0xe1, 0x23, 0x9e, 0x8a, 0xa9, 0xd6, 0x90, 0xa7, 0xdc, 0x9e, 0x2b, 0x9d, 0x8d, 0x9a, 0x8f,
	0x07, 0xc3, 0x3e, 0x21, 0xa3, 0x1d, 0x9e, 0xe7, 0xa9, 0x08, 0xdd, 0x6b, 0xec, 0x7f, 0x61, 0x94,
	0x3c, 0x7c, 0x0d, 0x09, 0x0e, 0xca, 0x90, 0x07, 0xf4, 0xbd, 0x00, 0x6d, 0xa1, 0x25, 0x46, 0x65,
	0xb4, 0x8b, 0x9f, 0xca, 0xd3, 0xc9, 0xb5, 0x99, 0x0c, 0xaa, 0xa0, 0x83, 0x77, 0x68, 0xf3, 0x60,
	0x38, 0x62, 0x6f, 0xd3, 0x7b, 0x67, 0xa8, 0x5f, 0xa2, 0x86, 0x13, 0xad, 0x95, 0x5e, 0x6d, 0x3f,
	0x58, 0x6c, 0x3f, 0x61, 0xbb, 0x74, 0xeb, 0x98, 0x47, 0xf0, 0x21, 0xb7, 0x38, 0xe3, 0x97, 0xd5,
	0xee, 0x74, 0xdd, 0xfd, 0x31, 0x3c, 0xf9, 0x27, 0x00, 0x00, 0xff, 0xff, 0xfd, 0xbe, 0x52, 0x9e,
	0x88, 0x06, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// RecruiterClient is the client API for Recruiter service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type RecruiterClient interface {
	/// Creates a company from a company message. Returns created company with
	// ok response
	CreateCompany(ctx context.Context, in *Company, opts ...grpc.CallOption) (*CompanyResponse, error)
	/// Reads a company, queried by company code. Returns company with ok response
	ReadCompany(ctx context.Context, in *CompanyRequest, opts ...grpc.CallOption) (*CompanyResponse, error)
	/// Updates a student's name or dorm. Specified by `changeDorm` boolean.
	// Returns new student.
	UpdateCompany(ctx context.Context, in *CompanyRequest, opts ...grpc.CallOption) (*CompanyResponse, error)
	/// Deletes a registration queried by id and returns the deleted student
	DeleteCompany(ctx context.Context, in *CompanyRequest, opts ...grpc.CallOption) (*CompanyResponse, error)
	/// Lists all the registered companies. Returns a stream of companies
	ListCompanies(ctx context.Context, in *Void, opts ...grpc.CallOption) (Recruiter_ListCompaniesClient, error)
	/// Removes all registered companies
	ClearCompanies(ctx context.Context, in *Void, opts ...grpc.CallOption) (*Void, error)
}

type recruiterClient struct {
	cc *grpc.ClientConn
}

func NewRecruiterClient(cc *grpc.ClientConn) RecruiterClient {
	return &recruiterClient{cc}
}

func (c *recruiterClient) CreateCompany(ctx context.Context, in *Company, opts ...grpc.CallOption) (*CompanyResponse, error) {
	out := new(CompanyResponse)
	err := c.cc.Invoke(ctx, "/recruiter.Recruiter/CreateCompany", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *recruiterClient) ReadCompany(ctx context.Context, in *CompanyRequest, opts ...grpc.CallOption) (*CompanyResponse, error) {
	out := new(CompanyResponse)
	err := c.cc.Invoke(ctx, "/recruiter.Recruiter/ReadCompany", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *recruiterClient) UpdateCompany(ctx context.Context, in *CompanyRequest, opts ...grpc.CallOption) (*CompanyResponse, error) {
	out := new(CompanyResponse)
	err := c.cc.Invoke(ctx, "/recruiter.Recruiter/UpdateCompany", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *recruiterClient) DeleteCompany(ctx context.Context, in *CompanyRequest, opts ...grpc.CallOption) (*CompanyResponse, error) {
	out := new(CompanyResponse)
	err := c.cc.Invoke(ctx, "/recruiter.Recruiter/DeleteCompany", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *recruiterClient) ListCompanies(ctx context.Context, in *Void, opts ...grpc.CallOption) (Recruiter_ListCompaniesClient, error) {
	stream, err := c.cc.NewStream(ctx, &_Recruiter_serviceDesc.Streams[0], "/recruiter.Recruiter/ListCompanies", opts...)
	if err != nil {
		return nil, err
	}
	x := &recruiterListCompaniesClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type Recruiter_ListCompaniesClient interface {
	Recv() (*CompanyResponse, error)
	grpc.ClientStream
}

type recruiterListCompaniesClient struct {
	grpc.ClientStream
}

func (x *recruiterListCompaniesClient) Recv() (*CompanyResponse, error) {
	m := new(CompanyResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *recruiterClient) ClearCompanies(ctx context.Context, in *Void, opts ...grpc.CallOption) (*Void, error) {
	out := new(Void)
	err := c.cc.Invoke(ctx, "/recruiter.Recruiter/ClearCompanies", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// RecruiterServer is the server API for Recruiter service.
type RecruiterServer interface {
	/// Creates a company from a company message. Returns created company with
	// ok response
	CreateCompany(context.Context, *Company) (*CompanyResponse, error)
	/// Reads a company, queried by company code. Returns company with ok response
	ReadCompany(context.Context, *CompanyRequest) (*CompanyResponse, error)
	/// Updates a student's name or dorm. Specified by `changeDorm` boolean.
	// Returns new student.
	UpdateCompany(context.Context, *CompanyRequest) (*CompanyResponse, error)
	/// Deletes a registration queried by id and returns the deleted student
	DeleteCompany(context.Context, *CompanyRequest) (*CompanyResponse, error)
	/// Lists all the registered companies. Returns a stream of companies
	ListCompanies(*Void, Recruiter_ListCompaniesServer) error
	/// Removes all registered companies
	ClearCompanies(context.Context, *Void) (*Void, error)
}

// UnimplementedRecruiterServer can be embedded to have forward compatible implementations.
type UnimplementedRecruiterServer struct {
}

func (*UnimplementedRecruiterServer) CreateCompany(ctx context.Context, req *Company) (*CompanyResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateCompany not implemented")
}
func (*UnimplementedRecruiterServer) ReadCompany(ctx context.Context, req *CompanyRequest) (*CompanyResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ReadCompany not implemented")
}
func (*UnimplementedRecruiterServer) UpdateCompany(ctx context.Context, req *CompanyRequest) (*CompanyResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateCompany not implemented")
}
func (*UnimplementedRecruiterServer) DeleteCompany(ctx context.Context, req *CompanyRequest) (*CompanyResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteCompany not implemented")
}
func (*UnimplementedRecruiterServer) ListCompanies(req *Void, srv Recruiter_ListCompaniesServer) error {
	return status.Errorf(codes.Unimplemented, "method ListCompanies not implemented")
}
func (*UnimplementedRecruiterServer) ClearCompanies(ctx context.Context, req *Void) (*Void, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ClearCompanies not implemented")
}

func RegisterRecruiterServer(s *grpc.Server, srv RecruiterServer) {
	s.RegisterService(&_Recruiter_serviceDesc, srv)
}

func _Recruiter_CreateCompany_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Company)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(RecruiterServer).CreateCompany(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/recruiter.Recruiter/CreateCompany",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(RecruiterServer).CreateCompany(ctx, req.(*Company))
	}
	return interceptor(ctx, in, info, handler)
}

func _Recruiter_ReadCompany_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CompanyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(RecruiterServer).ReadCompany(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/recruiter.Recruiter/ReadCompany",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(RecruiterServer).ReadCompany(ctx, req.(*CompanyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Recruiter_UpdateCompany_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CompanyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(RecruiterServer).UpdateCompany(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/recruiter.Recruiter/UpdateCompany",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(RecruiterServer).UpdateCompany(ctx, req.(*CompanyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Recruiter_DeleteCompany_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CompanyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(RecruiterServer).DeleteCompany(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/recruiter.Recruiter/DeleteCompany",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(RecruiterServer).DeleteCompany(ctx, req.(*CompanyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Recruiter_ListCompanies_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(Void)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(RecruiterServer).ListCompanies(m, &recruiterListCompaniesServer{stream})
}

type Recruiter_ListCompaniesServer interface {
	Send(*CompanyResponse) error
	grpc.ServerStream
}

type recruiterListCompaniesServer struct {
	grpc.ServerStream
}

func (x *recruiterListCompaniesServer) Send(m *CompanyResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _Recruiter_ClearCompanies_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Void)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(RecruiterServer).ClearCompanies(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/recruiter.Recruiter/ClearCompanies",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(RecruiterServer).ClearCompanies(ctx, req.(*Void))
	}
	return interceptor(ctx, in, info, handler)
}

var _Recruiter_serviceDesc = grpc.ServiceDesc{
	ServiceName: "recruiter.Recruiter",
	HandlerType: (*RecruiterServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CreateCompany",
			Handler:    _Recruiter_CreateCompany_Handler,
		},
		{
			MethodName: "ReadCompany",
			Handler:    _Recruiter_ReadCompany_Handler,
		},
		{
			MethodName: "UpdateCompany",
			Handler:    _Recruiter_UpdateCompany_Handler,
		},
		{
			MethodName: "DeleteCompany",
			Handler:    _Recruiter_DeleteCompany_Handler,
		},
		{
			MethodName: "ClearCompanies",
			Handler:    _Recruiter_ClearCompanies_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "ListCompanies",
			Handler:       _Recruiter_ListCompanies_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "proto/recruiter.proto",
}