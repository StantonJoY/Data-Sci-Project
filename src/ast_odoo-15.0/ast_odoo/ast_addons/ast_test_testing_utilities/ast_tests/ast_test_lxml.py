Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.xml_utils',
            names=[alias(name='_check_with_xsd', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        ImportFrom(
            module='lxml.etree',
            names=[alias(name='XMLSchemaError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestLXML',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_lxml_import_from_filestore',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='resolver_schema_int', ctx=Store())],
                            value=Constant(value=b'\n            <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"\n                        xmlns:etype="http://codespeak.net/lxml/test/external">\n                <xsd:import namespace="http://codespeak.net/lxml/test/external" schemaLocation="imported_schema.xsd"/>\n                <xsd:element name="a" type="etype:AType"/>\n            </xsd:schema>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='incomplete_schema_int', ctx=Store())],
                            value=Constant(value=b'\n            <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"\n                        xmlns:etype="http://codespeak.net/lxml/test/external">\n                <xsd:import namespace="http://codespeak.net/lxml/test/external" schemaLocation="non_existing_schema.xsd"/>\n                <xsd:element name="a" type="etype:AType"/>\n            </xsd:schema>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='imported_schema', ctx=Store())],
                            value=Constant(value=b'\n            <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"\n                        targetNamespace="http://codespeak.net/lxml/test/external">\n                <xsd:complexType name="AType">\n                    <xsd:sequence><xsd:element name="b" type="xsd:string" minOccurs="0" maxOccurs="unbounded"/></xsd:sequence>\n                </xsd:complexType>\n            </xsd:schema>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.attachment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='datas', kind=None),
                                                    Constant(value='name', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='resolver_schema_int', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='resolver_schema_int.xsd', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='datas', kind=None),
                                                    Constant(value='name', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='incomplete_schema_int', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='incomplete_schema_int.xsd', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='datas', kind=None),
                                                    Constant(value='name', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='imported_schema', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='imported_schema.xsd', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='_check_with_xsd', ctx=Load()),
                                args=[
                                    Constant(value='<a><b></b></a>', kind=None),
                                    Constant(value='resolver_schema_int.xsd', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='XMLSchemaError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_check_with_xsd', ctx=Load()),
                                        args=[
                                            Constant(value='<a><b></b></a>', kind=None),
                                            Constant(value='incomplete_schema_int.xsd', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='FileNotFoundError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_check_with_xsd', ctx=Load()),
                                        args=[
                                            Constant(value='<a><b></b></a>', kind=None),
                                            Constant(value='non_existing_schema.xsd', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
