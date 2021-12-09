Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        ImportFrom(
            module='PyPDF2',
            names=[
                alias(name='PdfFileReader', asname=None),
                alias(name='PdfFileWriter', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='reportlab.pdfgen',
            names=[alias(name='canvas', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='request', asname=None),
                alias(name='route', asname=None),
                alias(name='Controller', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='HrFleet',
            bases=[Name(id='Controller', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='get_claim_report_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='employee_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='has_group',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='fleet.fleet_group_manager', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='not_found',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='employee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.employee', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='employee_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_ids', ctx=Store())],
                            value=Attribute(
                                value=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='employee', ctx=Load()),
                                            attr='user_id',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    op=BitOr(),
                                    right=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='employee', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='address_home_id',
                                        ctx=Load(),
                                    ),
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='employee', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='partner_ids', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='not_found',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='car_assignation_logs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='fleet.vehicle.assignation.log', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='driver_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='partner_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='doc_list', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.attachment', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_model', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='fleet.vehicle.assignation.log', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='car_assignation_logs', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='create_date', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='writer', ctx=Store())],
                            value=Call(
                                func=Name(id='PdfFileWriter', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='font', ctx=Store())],
                            value=Constant(value='Helvetica', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='normal_font_size', ctx=Store())],
                            value=Constant(value=14, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='document', ctx=Store()),
                            iter=Name(id='doc_list', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='car_line_doc', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='fleet.vehicle.assignation.log', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='document', ctx=Load()),
                                                attr='res_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='reader', ctx=Store())],
                                            value=Call(
                                                func=Name(id='PdfFileReader', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='io', ctx=Load()),
                                                            attr='BytesIO',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='base64', ctx=Load()),
                                                                    attr='b64decode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='document', ctx=Load()),
                                                                        attr='datas',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='strict',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='overwriteWarnings',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[Continue()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Assign(
                                    targets=[Name(id='width', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='reader', ctx=Load()),
                                                                attr='getPage',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=0, kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='mediaBox',
                                                        ctx=Load(),
                                                    ),
                                                    attr='getUpperRight_x',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='height', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='reader', ctx=Load()),
                                                                attr='getPage',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=0, kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='mediaBox',
                                                        ctx=Load(),
                                                    ),
                                                    attr='getUpperRight_y',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='header', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='can', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='canvas', ctx=Load()),
                                            attr='Canvas',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='header', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='can', ctx=Load()),
                                            attr='setFont',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='font', ctx=Load()),
                                            Name(id='normal_font_size', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='can', ctx=Load()),
                                            attr='setFillColorRGB',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='car_name', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='car_line_doc', ctx=Load()),
                                            attr='vehicle_id',
                                            ctx=Load(),
                                        ),
                                        attr='display_name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='date_start', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='car_line_doc', ctx=Load()),
                                        attr='date_start',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='date_end', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='car_line_doc', ctx=Load()),
                                                attr='date_end',
                                                ctx=Load(),
                                            ),
                                            Constant(value='...', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='text_to_print', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='%(car_name)s (driven from: %(date_start)s to %(date_end)s)', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='car_name',
                                                value=Name(id='car_name', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='date_start',
                                                value=Name(id='date_start', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='date_end',
                                                value=Name(id='date_end', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='can', ctx=Load()),
                                            attr='drawCentredString',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='width', ctx=Load()),
                                                op=Div(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                            BinOp(
                                                left=Name(id='height', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='normal_font_size', ctx=Load()),
                                            ),
                                            Name(id='text_to_print', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='can', ctx=Load()),
                                            attr='save',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='header_pdf', ctx=Store())],
                                    value=Call(
                                        func=Name(id='PdfFileReader', ctx=Load()),
                                        args=[Name(id='header', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='overwriteWarnings',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='page_number', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='reader', ctx=Load()),
                                                    attr='getNumPages',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='page', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='reader', ctx=Load()),
                                                    attr='getPage',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='page_number', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='page', ctx=Load()),
                                                    attr='mergePage',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='header_pdf', ctx=Load()),
                                                            attr='getPage',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=0, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='writer', ctx=Load()),
                                                    attr='addPage',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='page', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='_buffer', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='_buffer', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='merged_pdf', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_buffer', ctx=Load()),
                                    attr='getvalue',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_buffer', ctx=Load()),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='pdfhttpheaders', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='Content-Type', kind=None),
                                            Constant(value='application/pdf', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='Content-Length', kind=None),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='merged_pdf', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[Name(id='merged_pdf', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='headers',
                                        value=Name(id='pdfhttpheaders', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[
                                List(
                                    elts=[Constant(value='/fleet/print_claim_report/<int:employee_id>', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
