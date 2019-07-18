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
// Represents a company with a name, code, number of job openings,
// and brokerage status
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
// A request made by a client who specifies a unique company code. Fields 2-4
// are set when updating a company's details.
type CompanyRequest struct {
	// unique id for each company
	CompanyCode int32 `protobuf:"varint,1,opt,name=companyCode,proto3" json:"companyCode,omitempty"`
	// name of the company
	CompanyName string `protobuf:"bytes,2,opt,name=companyName,proto3" json:"companyName,omitempty"`
	// how many jobs are available
	NumOpenings int32 `protobuf:"varint,3,opt,name=numOpenings,proto3" json:"numOpenings,omitempty"`
	// determines if the company is brokerage
	IsBrokerage bool `protobuf:"varint,4,opt,name=isBrokerage,proto3" json:"isBrokerage,omitempty"`
	// True if transaction is successful, false otherwise
	Ok                   bool     `protobuf:"varint,5,opt,name=ok,proto3" json:"ok,omitempty"`
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

func (m *CompanyRequest) GetCompanyName() string {
	if m != nil {
		return m.CompanyName
	}
	return ""
}

func (m *CompanyRequest) GetNumOpenings() int32 {
	if m != nil {
		return m.NumOpenings
	}
	return 0
}

func (m *CompanyRequest) GetIsBrokerage() bool {
	if m != nil {
		return m.IsBrokerage
	}
	return false
}

func (m *CompanyRequest) GetOk() bool {
	if m != nil {
		return m.Ok
	}
	return false
}

//*
// A response sent by a server, returning a `Company` message and a boolean field
// indicating a successful transaction
type CompanyResponse struct {
	// The deleted, created, or retrieved company
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
	// 751 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xcc, 0x55, 0x4f, 0x8b, 0x23, 0x45,
	0x1c, 0xa5, 0x92, 0xd9, 0x64, 0x53, 0xd9, 0x64, 0x96, 0x82, 0x68, 0xb6, 0x59, 0xe1, 0x67, 0xf0,
	0x30, 0x84, 0x9d, 0x74, 0x36, 0xeb, 0x5c, 0x06, 0x3c, 0x24, 0x9d, 0x41, 0x76, 0x15, 0x07, 0x7a,
	0x76, 0x05, 0xbd, 0x55, 0xd2, 0xbf, 0xe9, 0x94, 0xd3, 0x5d, 0xd5, 0x56, 0x55, 0x4f, 0x1c, 0x44,
	0x10, 0x3f, 0x80, 0x60, 0x04, 0x0f, 0xfa, 0x05, 0xc4, 0xa3, 0x17, 0x3f, 0x88, 0x9f, 0x40, 0xd0,
	0x0f, 0xe1, 0x4d, 0xd2, 0x9d, 0xce, 0xf4, 0xfc, 0x61, 0x0e, 0x7a, 0x70, 0x4f, 0x49, 0x7e, 0xf5,
	0xf2, 0xde, 0xfb, 0xbd, 0x57, 0xe9, 0xd0, 0x4e, 0xa2, 0x95, 0x55, 0xae, 0xc6, 0xb9, 0x4e, 0x85,
	0x45, 0x3d, 0xc8, 0x3e, 0xb3, 0xc6, 0x76, 0xe0, 0x3c, 0x0e, 0x95, 0x0a, 0x23, 0x74, 0x79, 0x22,
	0x5c, 0x2e, 0xa5, 0xb2, 0xdc, 0x0a, 0x25, 0x4d, 0x0e, 0x74, 0x9e, 0x64, 0x2f, 0xf3, 0xfd, 0x10,
	0xe5, 0xbe, 0x59, 0xf2, 0x30, 0x44, 0xed, 0xaa, 0x24, 0x43, 0xdc, 0x44, 0xf7, 0x6a, 0x74, 0xe7,
	0x63, 0x25, 0x82, 0xde, 0x77, 0x84, 0xd6, 0x3d, 0x15, 0x27, 0x5c, 0x5e, 0x30, 0xa0, 0xcd, 0x79,
	0xfe, 0xd6, 0x53, 0x01, 0x76, 0x09, 0x90, 0xbd, 0x7b, 0x7e, 0x79, 0x54, 0x42, 0x7c, 0xc4, 0x63,
	0xec, 0x56, 0x80, 0xec, 0x35, 0xfc, 0xf2, 0x68, 0x8d, 0x90, 0x69, 0x7c, 0x9c, 0xa0, 0x14, 0x32,
	0x34, 0xdd, 0x6a, 0xce, 0x51, 0x1a, 0xad, 0x11, 0xc2, 0x4c, 0xb4, 0x3a, 0x43, 0xcd, 0x43, 0xec,
	0xee, 0x00, 0xd9, 0xbb, 0xef, 0x97, 0x47, 0xbd, 0x9f, 0x09, 0x6d, 0x6f, 0x3c, 0xf9, 0xf8, 0x79,
	0x8a, 0xc6, 0xbe, 0x2e, 0xd6, 0x58, 0x9b, 0x56, 0xd4, 0x59, 0xf7, 0x5e, 0x76, 0x50, 0x51, 0x67,
	0xbd, 0x63, 0xba, 0xbb, 0x75, 0x6a, 0x12, 0x25, 0x0d, 0xb2, 0x27, 0xb4, 0xbe, 0x51, 0xcd, 0x6c,
	0x36, 0x47, 0x6c, 0x70, 0xd9, 0x69, 0x01, 0x2e, 0x20, 0x1b, 0xc2, 0x4a, 0x41, 0x38, 0xfa, 0xa5,
	0x4e, 0x1b, 0x7e, 0x01, 0x67, 0x3f, 0x11, 0xda, 0xf2, 0x34, 0x72, 0x8b, 0x45, 0x47, 0xb7, 0x90,
	0x39, 0xce, 0x2d, 0x02, 0x1b, 0x37, 0xbd, 0x4f, 0x57, 0x63, 0x8f, 0xb5, 0x4e, 0xd2, 0x38, 0xe6,
	0xfa, 0xe2, 0x10, 0x2c, 0x1a, 0xeb, 0x3c, 0x9c, 0xa2, 0x99, 0x6b, 0x91, 0xdd, 0x0d, 0x78, 0x89,
	0xc6, 0xbe, 0x00, 0x5a, 0x1d, 0x0d, 0x87, 0xec, 0x11, 0xdd, 0x3d, 0x3e, 0x47, 0xbd, 0xd4, 0xc2,
	0xa2, 0x81, 0x4f, 0x8e, 0x8e, 0x5e, 0xb2, 0x1a, 0xdd, 0xf9, 0xb1, 0x42, 0xea, 0xdf, 0xfc, 0xfe,
	0xe7, 0xf7, 0x95, 0x76, 0xaf, 0xe1, 0x6a, 0x0c, 0x85, 0xb1, 0xa8, 0x0f, 0x49, 0x9f, 0xfd, 0x4d,
	0x68, 0xd3, 0x47, 0x1e, 0x14, 0xde, 0x1e, 0xdd, 0xe6, 0x23, 0xeb, 0xef, 0x4e, 0x8b, 0xbf, 0x92,
	0xd5, 0xf8, 0x5b, 0xc2, 0xf6, 0x37, 0x73, 0x10, 0x06, 0xa4, 0xb2, 0x20, 0x24, 0xd8, 0x05, 0x42,
	0xc0, 0x2d, 0x9f, 0x71, 0x83, 0x03, 0xf0, 0xb2, 0x5b, 0x0c, 0x01, 0x46, 0x68, 0xd1, 0xe9, 0x17,
	0xf0, 0xa5, 0xb0, 0x0b, 0xf8, 0xb2, 0x74, 0x15, 0xbe, 0x82, 0x40, 0x61, 0xce, 0x81, 0x5f, 0x08,
	0x63, 0xdf, 0x7e, 0xf1, 0x94, 0x56, 0xdf, 0x1d, 0x0e, 0x59, 0x9f, 0x42, 0x69, 0xbd, 0x00, 0x4f,
	0x79, 0x1a, 0x59, 0x58, 0x2e, 0x50, 0xe6, 0xa4, 0x42, 0x86, 0x57, 0xf6, 0x75, 0x58, 0xd7, 0xcd,
	0x79, 0x05, 0x1a, 0xf7, 0x8a, 0x04, 0x5b, 0xd0, 0xd6, 0xab, 0x24, 0x28, 0x15, 0xf3, 0x2f, 0x97,
	0x87, 0x5c, 0xc9, 0xe9, 0xb8, 0x69, 0x46, 0x77, 0x55, 0x66, 0x9d, 0xf2, 0xd7, 0x15, 0xda, 0x9a,
	0x66, 0x3b, 0xff, 0x47, 0xa9, 0xdf, 0xc8, 0x6a, 0xfc, 0x03, 0x61, 0x07, 0xcf, 0xa7, 0xb0, 0xe0,
	0x79, 0x3e, 0x33, 0x44, 0x09, 0x45, 0xa5, 0x18, 0xc0, 0xa9, 0xd2, 0xb0, 0x50, 0xa9, 0x11, 0x32,
	0xfc, 0x1f, 0xf2, 0x7e, 0xb3, 0xdf, 0x71, 0x73, 0xb5, 0x6b, 0x61, 0xfb, 0xb4, 0xf5, 0xa1, 0x30,
	0xd6, 0x2b, 0xba, 0x60, 0xbb, 0xa5, 0x35, 0xd7, 0x8f, 0xb1, 0x3b, 0xf7, 0x66, 0x19, 0xf9, 0x03,
	0x46, 0x2f, 0xcb, 0x1c, 0x12, 0x36, 0xa1, 0x6d, 0x2f, 0x42, 0xae, 0xef, 0x20, 0xbd, 0x3e, 0xe8,
	0xb5, 0x33, 0xa6, 0xfb, 0xfd, 0x9a, 0x3b, 0x5f, 0x7f, 0x75, 0xf2, 0x17, 0x59, 0x8d, 0xff, 0x20,
	0x6c, 0x4a, 0xdf, 0x3b, 0x11, 0x71, 0x12, 0x21, 0x04, 0x18, 0x2b, 0xf0, 0xfc, 0x57, 0x53, 0xe0,
	0x49, 0x92, 0xa5, 0xb9, 0x95, 0x84, 0x85, 0xd0, 0x42, 0x86, 0xa0, 0x24, 0x7c, 0xc0, 0x23, 0x31,
	0xd3, 0x1a, 0x92, 0x88, 0xdb, 0x53, 0xa5, 0xe3, 0x51, 0xf5, 0xe9, 0x60, 0xd8, 0x27, 0x64, 0xf4,
	0x90, 0x27, 0x49, 0x24, 0xe6, 0xd9, 0x83, 0xda, 0xfd, 0xcc, 0x28, 0x79, 0x78, 0x63, 0xe2, 0x1f,
	0xe4, 0xd9, 0x0e, 0xe8, 0x3b, 0x3e, 0xda, 0x54, 0x4b, 0x0c, 0xf2, 0x44, 0xd7, 0xbf, 0x95, 0xe7,
	0xd3, 0x6b, 0x55, 0x0c, 0x8a, 0x7c, 0xfd, 0xb7, 0x68, 0xf5, 0x60, 0x38, 0x62, 0x6f, 0xd0, 0x07,
	0x27, 0xa8, 0xcf, 0x51, 0xc3, 0x91, 0xd6, 0x4a, 0x6f, 0x8f, 0x1f, 0xaf, 0x8f, 0x9f, 0xb1, 0x0e,
	0x6d, 0x4e, 0x78, 0x00, 0xef, 0x73, 0x8b, 0x4b, 0x7e, 0x51, 0x9c, 0xce, 0x6a, 0xd9, 0x7f, 0xc6,
	0xb3, 0x7f, 0x02, 0x00, 0x00, 0xff, 0xff, 0xef, 0x38, 0x2a, 0xb7, 0xa3, 0x06, 0x00, 0x00,
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
	// Creates a company from a company message. Returns created company with
	// ok response
	CreateCompany(ctx context.Context, in *Company, opts ...grpc.CallOption) (*CompanyResponse, error)
	// Reads a company, queried by company code. Returns company with ok response
	ReadCompany(ctx context.Context, in *CompanyRequest, opts ...grpc.CallOption) (*CompanyResponse, error)
	// Updates a company's name, number of openings, or brokerage. Returns the
	// updated company
	UpdateCompany(ctx context.Context, in *CompanyRequest, opts ...grpc.CallOption) (*CompanyResponse, error)
	// Deletes a company queried by id and returns the deleted company
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
	// Creates a company from a company message. Returns created company with
	// ok response
	CreateCompany(context.Context, *Company) (*CompanyResponse, error)
	// Reads a company, queried by company code. Returns company with ok response
	ReadCompany(context.Context, *CompanyRequest) (*CompanyResponse, error)
	// Updates a company's name, number of openings, or brokerage. Returns the
	// updated company
	UpdateCompany(context.Context, *CompanyRequest) (*CompanyResponse, error)
	// Deletes a company queried by id and returns the deleted company
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
