Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='namedtuple', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='freezegun', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.account_edi.tests.common',
            names=[alias(name='AccountEdiTestCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.l10n_it_edi.tools.remove_signature',
            names=[alias(name='remove_signature', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='PecMailServerTests',
            bases=[Name(id='AccountEdiTestCommon', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Main test class for the l10n_it_edi vendor bills XML import from a PEC mail account', kind=None),
                ),
                Assign(
                    targets=[Name(id='fake_test_content', ctx=Store())],
                    value=Constant(value='<?xml version="1.0" encoding="UTF-8"?>\n        <p:FatturaElettronica versione="FPR12" xmlns:ds="http://www.w3.org/2000/09/xmldsig#"\n        xmlns:p="http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2"\n        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n        xsi:schemaLocation="http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2 http://www.fatturapa.gov.it/export/fatturazione/sdi/fatturapa/v1.2/Schema_del_file_xml_FatturaPA_versione_1.2.xsd">\n          <FatturaElettronicaHeader>\n            <CessionarioCommittente>\n              <DatiAnagrafici>\n                <CodiceFiscale>01234560157</CodiceFiscale>\n              </DatiAnagrafici>\n            </CessionarioCommittente>\n          </FatturaElettronicaHeader>\n          <FatturaElettronicaBody>\n            <DatiGenerali>\n              <DatiGeneraliDocumento>\n                <TipoDocumento>TD02</TipoDocumento>\n              </DatiGeneraliDocumento>\n            </DatiGenerali>\n          </FatturaElettronicaBody>\n        </p:FatturaElettronica>', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Setup the test class with a PEC mail server and a fake fatturaPA content ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='chart_template_ref',
                                        value=Constant(value='l10n_it.l10n_it_chart_template_generic', kind=None),
                                    ),
                                    keyword(
                                        arg='edi_format_ref',
                                        value=Constant(value='l10n_it_edi.edi_fatturaPA', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data_2',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    attr='l10n_it_codice_fiscale',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='IT01234560157', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='invoice_filename1',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='IT01234567890_FPR01.xml', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='invoice_filename2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='IT01234567890_FPR02.xml', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='signed_invoice_filename',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='IT01234567890_FPR01.xml.p7m', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='invoice_content',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_get_test_file_content',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='invoice_filename1',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='signed_invoice_content',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_get_test_file_content',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='signed_invoice_filename',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='invoice',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='ref', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Constant(value='01234567890', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='attachment',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
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
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='raw', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='res_model', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='invoice_filename1',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='invoice_content',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='invoice',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='account.move', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='edi_document',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.edi.document', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='edi_format_id', kind=None),
                                            Constant(value='move_id', kind=None),
                                            Constant(value='attachment_id', kind=None),
                                            Constant(value='state', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='edi_format',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='invoice',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='attachment',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='sent', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='server',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='fetchmail.server', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='server_type', kind=None),
                                            Constant(value='l10n_it_is_pec', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_server', kind=None),
                                            Constant(value='imap', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_test_file_content',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Get the content of a test file inside this module ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='l10n_it_edi/tests/expected_xmls/', kind=None),
                                op=Add(),
                                right=Name(id='filename', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='file_open',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='mode',
                                                value=Constant(value='rb', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='test_file', ctx=Store()),
                                ),
                            ],
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='test_file', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create an invoice from given attachment content ', kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='server',
                                                    ctx=Load(),
                                                ),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            Constant(value='commit', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='return_value',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='filename', ctx=Load()),
                                            attr='endswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.p7m', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Name(id='remove_signature', ctx=Load()),
                                                args=[Name(id='content', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='server',
                                                ctx=Load(),
                                            ),
                                            attr='_create_invoice_from_mail',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='content', ctx=Load()),
                                            Name(id='filename', ctx=Load()),
                                            Constant(value='fake@address.be', kind=None),
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
                FunctionDef(
                    name='test_receive_vendor_bill',
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
                        Expr(
                            value=Constant(value=' Test a sample e-invoice file from https://www.fatturapa.gov.it/export/documenti/fatturapa/v1.2/IT01234567890_FPR01.xml ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='invoices', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_invoice',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice_content',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice_filename2',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='invoices', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_receive_signed_vendor_bill',
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
                        Expr(
                            value=Constant(value=' Test a signed (P7M) sample e-invoice file from https://www.fatturapa.gov.it/export/documenti/fatturapa/v1.2/IT01234567890_FPR01.xml ', kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='freezegun', ctx=Load()),
                                            attr='freeze_time',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2020-04-06', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoices', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='signed_invoice_content',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='signed_invoice_filename',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRecordValues',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoices', ctx=Load()),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='invoice_date', kind=None),
                                                            Constant(value='ref', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='company',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='BILL/2014/12/0001', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='datetime', ctx=Load()),
                                                                    attr='date',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value=2014, kind=None),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value=18, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='01234567890', kind=None),
                                                        ],
                                                    ),
                                                ],
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
                FunctionDef(
                    name='test_receive_same_vendor_bill_twice',
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
                        Expr(
                            value=Constant(value=' Test that the second time we are receiving a PEC mail with the same attachment, the second is discarded ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='fake_test_content',
                                        ctx=Load(),
                                    ),
                                    attr='encode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='result', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value=True, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='content', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='invoice_filename2',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='result', ctx=Load()),
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[Name(id='invoice', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_test_receipt',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='receipt_type', annotation=None, type_comment=None),
                            arg(arg='source_state', annotation=None, type_comment=None),
                            arg(arg='destination_state', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Test a receipt from the ones in the module's test files ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    attr='l10n_it_send_state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='source_state', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='receipt_filename', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='IT01234567890_FPR01_%s_001.xml', kind=None),
                                op=Mod(),
                                right=Name(id='receipt_type', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='receipt_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_test_file_content',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='receipt_filename', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='create_mail_attachment', ctx=Store())],
                            value=Call(
                                func=Name(id='namedtuple', ctx=Load()),
                                args=[
                                    Constant(value='Attachment', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='fname', kind=None),
                                            Constant(value='content', kind=None),
                                            Constant(value='info', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='receipt_mail_attachment', ctx=Store())],
                            value=Call(
                                func=Name(id='create_mail_attachment', ctx=Load()),
                                args=[
                                    Name(id='receipt_filename', ctx=Load()),
                                    Name(id='receipt_content', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='server',
                                                    ctx=Load(),
                                                ),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            Constant(value='commit', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='return_value',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='server',
                                                ctx=Load(),
                                            ),
                                            attr='_message_receipt_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='receipt_type', ctx=Load()),
                                            Name(id='receipt_mail_attachment', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='destination_state', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='edi_document',
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_ricevuta_consegna',
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
                        Expr(
                            value=Constant(value=' Test a receipt adapted from https://www.fatturapa.gov.it/export/documenti/messaggi/v1.0/IT01234567890_11111_RC_001.xml ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_test_receipt',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='RC', kind=None),
                                    Constant(value='sent', kind=None),
                                    Constant(value='delivered', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_decorrenza_termini',
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
                        Expr(
                            value=Constant(value=' Test a receipt adapted from https://www.fatturapa.gov.it/export/documenti/messaggi/v1.0/IT01234567890_11111_DT_001.xml ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_test_receipt',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='DT', kind=None),
                                    Constant(value='delivered', kind=None),
                                    Constant(value='delivered_expired', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install_l10n', kind=None),
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
