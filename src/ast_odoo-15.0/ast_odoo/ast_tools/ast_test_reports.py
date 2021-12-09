Module(
    body=[
        Expr(
            value=Constant(value=' Helper functions for reports testing.\n\n    Please /do not/ import this file by default, but only explicitly call it\n    through the code of python tests.\n', kind=None),
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='tempfile', asname=None)],
        ),
        ImportFrom(
            module='subprocess',
            names=[
                alias(name='Popen', asname=None),
                alias(name='PIPE', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='api', asname=None)],
            level=2,
        ),
        ImportFrom(
            module=None,
            names=[
                alias(name='ustr', asname=None),
                alias(name='config', asname=None),
            ],
            level=1,
        ),
        ImportFrom(
            module='safe_eval',
            names=[alias(name='safe_eval', asname=None)],
            level=1,
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
        Assign(
            targets=[Name(id='_test_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Constant(value='odoo.tests', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='try_report',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='uid', annotation=None, type_comment=None),
                    arg(arg='rname', annotation=None, type_comment=None),
                    arg(arg='ids', annotation=None, type_comment=None),
                    arg(arg='data', annotation=None, type_comment=None),
                    arg(arg='context', annotation=None, type_comment=None),
                    arg(arg='our_module', annotation=None, type_comment=None),
                    arg(arg='report_type', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Try to render a report <rname> with contents of ids\n\n        This function should also check for common pitfalls of reports.\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='context', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_test_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='  - Trying %s.create(%r)', kind=None),
                            Name(id='rname', ctx=Load()),
                            Name(id='ids', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='Environment',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='uid', ctx=Load()),
                            Name(id='context', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='ir.actions.report', kind=None),
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
                                            Constant(value='report_name', kind=None),
                                            Constant(value='=', kind=None),
                                            Name(id='rname', ctx=Load()),
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
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='report_id', ctx=Load()),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='Exception', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='Required report does not exist: %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='rname', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='res_data', ctx=Store()),
                                Name(id='res_format', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Name(id='report_id', ctx=Load()),
                            attr='_render',
                            ctx=Load(),
                        ),
                        args=[Name(id='ids', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='data',
                                value=Name(id='data', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='res_data', ctx=Load()),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='Report %s produced an empty result!', kind=None),
                                        op=Mod(),
                                        right=Name(id='rname', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='debug',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Have a %s report for %s, will examine it', kind=None),
                            Name(id='res_format', ctx=Load()),
                            Name(id='rname', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    test=Compare(
                        left=Name(id='res_format', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='pdf', kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='res_data', ctx=Load()),
                                    slice=Slice(
                                        lower=None,
                                        upper=Constant(value=5, kind=None),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value=b'%PDF-', kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Report %s produced a non-pdf header, %r', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='rname', ctx=Load()),
                                                        Subscript(
                                                            value=Name(id='res_data', ctx=Load()),
                                                            slice=Slice(
                                                                lower=None,
                                                                upper=Constant(value=10, kind=None),
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res_text', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='fd', ctx=Store()),
                                                Name(id='rfname', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tempfile', ctx=Load()),
                                            attr='mkstemp',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='suffix',
                                                value=Name(id='res_format', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fd', ctx=Load()),
                                            Name(id='res_data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='close',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='fd', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='proc', ctx=Store())],
                                    value=Call(
                                        func=Name(id='Popen', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='pdftotext', kind=None),
                                                    Constant(value='-enc', kind=None),
                                                    Constant(value='UTF-8', kind=None),
                                                    Constant(value='-nopgbrk', kind=None),
                                                    Name(id='rfname', ctx=Load()),
                                                    Constant(value='-', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='shell',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='stdout',
                                                value=Name(id='PIPE', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='stdout', ctx=Store()),
                                                Name(id='stderr', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='proc', ctx=Load()),
                                            attr='communicate',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='res_text', ctx=Store())],
                                    value=Call(
                                        func=Name(id='ustr', ctx=Load()),
                                        args=[Name(id='stdout', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rfname', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Unable to parse PDF report: install pdftotext to perform automated tests.', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='res_text', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=False, kind=None)],
                            ),
                            body=[
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='res_text', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='\n', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Constant(value='[[', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='line', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Constant(value='[ [', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='line', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Report %s may have bad expression near: "%s".', kind=None),
                                                            Name(id='rname', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='line', ctx=Load()),
                                                                slice=Slice(
                                                                    lower=Constant(value=80, kind=None),
                                                                    upper=None,
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Name(id='res_format', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='html', kind=None)],
                            ),
                            body=[Pass()],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Report %s produced a "%s" chunk, cannot examine it', kind=None),
                                            Name(id='rname', ctx=Load()),
                                            Name(id='res_format', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_test_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='  + Report %s produced correctly.', kind=None),
                            Name(id='rname', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='try_report_action',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='uid', annotation=None, type_comment=None),
                    arg(arg='action_id', annotation=None, type_comment=None),
                    arg(arg='active_model', annotation=None, type_comment=None),
                    arg(arg='active_ids', annotation=None, type_comment=None),
                    arg(arg='wiz_data', annotation=None, type_comment=None),
                    arg(arg='wiz_buttons', annotation=None, type_comment=None),
                    arg(arg='context', annotation=None, type_comment=None),
                    arg(arg='our_module', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value="Take an ir.actions.act_window and follow it until a report is produced\n\n        :param action_id: the integer id of an action, or a reference to xml id\n                of the act_window (can search [our_module.]+xml_id\n        :param active_model, active_ids: call the action as if it had been launched\n                from that model+ids (tree/form view action)\n        :param wiz_data: a dictionary of values to use in the wizard, if needed.\n                They will override (or complete) the default values of the\n                wizard form.\n        :param wiz_buttons: a list of button names, or button icon strings, which\n                should be preferred to press during the wizard.\n                Eg. 'OK' or 'fa-print'\n        :param our_module: the name of the calling module (string), like 'account'\n    ", kind=None),
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='our_module', ctx=Load()),
                            ),
                            Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='action_id', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='.', kind=None),
                                ops=[In()],
                                comparators=[Name(id='action_id', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='our_module', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='action_id', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='.', kind=None),
                                                Constant(value=1, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='context', ctx=Store())],
                    value=Call(
                        func=Name(id='dict', ctx=Load()),
                        args=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='context', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='Environment',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='uid', ctx=Load()),
                            Name(id='context', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='log_test',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='msg', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_test_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='  - ', kind=None),
                                        op=Add(),
                                        right=Name(id='msg', ctx=Load()),
                                    ),
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
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
                Assign(
                    targets=[Name(id='datas', ctx=Store())],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                If(
                    test=Name(id='active_model', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='datas', ctx=Load()),
                                    slice=Constant(value='model', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='active_model', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Name(id='active_ids', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='datas', ctx=Load()),
                                    slice=Constant(value='ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='active_ids', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='wiz_buttons', ctx=Load()),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='wiz_buttons', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='action_id', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='.', kind=None),
                                ops=[In()],
                                comparators=[Name(id='action_id', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='_', ctx=Store()),
                                                Name(id='act_xmlid', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='action_id', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='.', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='our_module', ctx=Load()),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='You cannot only specify action_id "%s" without a module name', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='action_id', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='act_xmlid', ctx=Store())],
                                    value=Name(id='action_id', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='action_id', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s.%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='our_module', ctx=Load()),
                                                Name(id='action_id', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='env', ctx=Load()),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Name(id='action_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='act_model', ctx=Store()),
                                        Name(id='act_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Name(id='action', ctx=Load()),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='action', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assert(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='action_id', ctx=Load()),
                                    Name(id='int', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='act_model', ctx=Store())],
                            value=Constant(value='ir.actions.act_window', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='act_id', ctx=Store())],
                            value=Name(id='action_id', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='act_xmlid', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='<%s>', kind=None),
                                op=Mod(),
                                right=Name(id='act_id', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
                FunctionDef(
                    name='_exec_action',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='action', annotation=None, type_comment=None),
                            arg(arg='datas', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='action', ctx=Load()),
                                            Name(id='bool', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Constant(value='type', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='action', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='env', ctx=Load()),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='datas', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='id', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='context', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='active_id', kind=None),
                                                    Constant(value='active_ids', kind=None),
                                                    Constant(value='active_model', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='datas', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='datas', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='ids', kind=None),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='datas', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='model', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='context1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='action', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='context', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='context1', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='context1', ctx=Store())],
                                    value=Call(
                                        func=Name(id='safe_eval', ctx=Load()),
                                        args=[
                                            Name(id='context1', ctx=Load()),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[Name(id='context', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context1', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='env', ctx=Store())],
                            value=Call(
                                func=Name(id='env', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='context',
                                        value=Name(id='context', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='ir.actions.act_window', kind=None),
                                            Constant(value='ir.actions.submenu', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='key', ctx=Store()),
                                    iter=Tuple(
                                        elts=[
                                            Constant(value='res_id', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='view_mode', kind=None),
                                            Constant(value='limit', kind=None),
                                            Constant(value='search_view', kind=None),
                                            Constant(value='search_view_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='datas', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='action', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='key', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='datas', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='key', ctx=Load()),
                                                            Constant(value=None, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='view_id', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='view_type', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='views', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='action', ctx=Load()),
                                                        slice=Constant(value='views', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='list', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='view_id', ctx=Store()),
                                                                Name(id='view_type', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='action', ctx=Load()),
                                                            slice=Constant(value='views', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='datas', ctx=Load()),
                                                            slice=Constant(value='view_mode', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='view_type', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='action', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='view_id', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='view_id', ctx=Store())],
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='action', ctx=Load()),
                                                                    slice=Constant(value='view_id', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='action', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='view_id', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='view_id', ctx=Store())],
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='action', ctx=Load()),
                                                            slice=Constant(value='view_id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='view_type', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Name(id='view_id', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='view_type', ctx=Store())],
                                                    value=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='env', ctx=Load()),
                                                                    slice=Constant(value='ir.ui.view', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='browse',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='view_id', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='type',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='view_type', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='action', ctx=Load()),
                                                                    slice=Constant(value='view_mode', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=',', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assert(
                                    test=Subscript(
                                        value=Name(id='datas', ctx=Load()),
                                        slice=Constant(value='res_model', kind=None),
                                        ctx=Load(),
                                    ),
                                    msg=Constant(value='Cannot use the view without a model', kind=None),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='log_test', ctx=Load()),
                                        args=[
                                            Constant(value='will emulate a %s view: %s#%s', kind=None),
                                            Name(id='view_type', ctx=Load()),
                                            Subscript(
                                                value=Name(id='datas', ctx=Load()),
                                                slice=Constant(value='res_model', kind=None),
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='view_id', ctx=Load()),
                                                    Constant(value='?', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='view_res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Subscript(
                                                    value=Name(id='datas', ctx=Load()),
                                                    slice=Constant(value='res_model', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='fields_view_get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='view_id', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='view_type',
                                                value=Name(id='view_type', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assert(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='view_res', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view_res', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='arch', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    msg=Constant(value='Did not return any arch for the view', kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='view_data', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='view_res', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='fields', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='view_data', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Subscript(
                                                            value=Name(id='datas', ctx=Load()),
                                                            slice=Constant(value='res_model', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='default_get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='view_res', ctx=Load()),
                                                                slice=Constant(value='fields', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='datas', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='form', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='view_data', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='datas', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='form', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='wiz_data', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='view_data', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='wiz_data', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='View data is: %r', kind=None),
                                            Name(id='view_data', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='fk', ctx=Store()),
                                            Name(id='field', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='view_res', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='fields', kind=None),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='field', ctx=Load()),
                                                            slice=Constant(value='type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='one2many', kind=None),
                                                                    Constant(value='many2many', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='view_data', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='fk', ctx=Load()),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='view_data', ctx=Load()),
                                                                slice=Name(id='fk', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='list', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(id='isinstance', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='view_data', ctx=Load()),
                                                                        slice=Name(id='fk', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='tuple', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='view_data', ctx=Load()),
                                                            slice=Name(id='fk', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=6, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Subscript(
                                                                        value=Name(id='view_data', ctx=Load()),
                                                                        slice=Name(id='fk', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='action_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        ImportFrom(
                                            module='xml.dom',
                                            names=[alias(name='minidom', asname=None)],
                                            level=0,
                                        ),
                                        Assign(
                                            targets=[Name(id='cancel_found', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='buttons', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='dom_doc', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='minidom', ctx=Load()),
                                                    attr='parseString',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='view_res', ctx=Load()),
                                                        slice=Constant(value='arch', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='action_name', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='action_name', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='dom_doc', ctx=Load()),
                                                                attr='documentElement',
                                                                ctx=Load(),
                                                            ),
                                                            attr='getAttribute',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='name', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        For(
                                            target=Name(id='button', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='dom_doc', ctx=Load()),
                                                    attr='getElementsByTagName',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='button', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='button_weight', ctx=Store())],
                                                    value=Constant(value=0, kind=None),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='button', ctx=Load()),
                                                                attr='getAttribute',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='special', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='cancel', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='cancel_found', ctx=Store())],
                                                            value=Constant(value=True, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Continue(),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='button', ctx=Load()),
                                                                attr='getAttribute',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='icon', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='fa-times-circle', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='cancel_found', ctx=Store())],
                                                            value=Constant(value=True, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Continue(),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='button', ctx=Load()),
                                                                attr='getAttribute',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='default_focus', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='1', kind=None)],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='button_weight', ctx=Store()),
                                                            op=Add(),
                                                            value=Constant(value=20, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='button', ctx=Load()),
                                                                attr='getAttribute',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='string', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='wiz_buttons', ctx=Load())],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='button_weight', ctx=Store()),
                                                            op=Add(),
                                                            value=Constant(value=30, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='button', ctx=Load()),
                                                                        attr='getAttribute',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='icon', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                ops=[In()],
                                                                comparators=[Name(id='wiz_buttons', ctx=Load())],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='button_weight', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Constant(value=10, kind=None),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                                Assign(
                                                    targets=[Name(id='string', ctx=Store())],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='button', ctx=Load()),
                                                                    attr='getAttribute',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='string', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            BinOp(
                                                                left=Constant(value='?%s', kind=None),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='buttons', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='buttons', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='string', kind=None),
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='weight', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='button', ctx=Load()),
                                                                            attr='getAttribute',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='name', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Name(id='string', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='button', ctx=Load()),
                                                                            attr='getAttribute',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='type', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Name(id='button_weight', ctx=Load()),
                                                                ],
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
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='Cannot resolve the view arch and locate the buttons!', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='exc_info',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='AssertionError', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='e', ctx=Load()),
                                                                    attr='args',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='datas', ctx=Load()),
                                            slice=Constant(value='res_id', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='datas', ctx=Load()),
                                                    slice=Constant(value='res_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='env', ctx=Load()),
                                                            slice=Subscript(
                                                                value=Name(id='datas', ctx=Load()),
                                                                slice=Constant(value='res_model', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        attr='create',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='view_data', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='buttons', ctx=Load()),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='AssertionError', ctx=Load()),
                                                args=[Constant(value="view form doesn't have any buttons to press!", kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='buttons', ctx=Load()),
                                            attr='sort',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='b', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Subscript(
                                                        value=Name(id='b', ctx=Load()),
                                                        slice=Constant(value='weight', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Buttons are: %s', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value=', ', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    ListComp(
                                                        elt=BinOp(
                                                            left=Constant(value='%s: %d', kind=None),
                                                            op=Mod(),
                                                            right=Tuple(
                                                                elts=[
                                                                    Subscript(
                                                                        value=Name(id='b', ctx=Load()),
                                                                        slice=Constant(value='string', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Name(id='b', ctx=Load()),
                                                                        slice=Constant(value='weight', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='b', ctx=Store()),
                                                                iter=Name(id='buttons', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                While(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='buttons', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='res', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='b', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='buttons', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='log_test', ctx=Load()),
                                                args=[
                                                    Constant(value='in the "%s" form, I will press the "%s" button.', kind=None),
                                                    Name(id='action_name', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='b', ctx=Load()),
                                                        slice=Constant(value='string', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value='type', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='log_test', ctx=Load()),
                                                        args=[
                                                            Constant(value='the "%s" button has no type, cannot use it', kind=None),
                                                            Subscript(
                                                                value=Name(id='b', ctx=Load()),
                                                                slice=Constant(value='string', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value='type', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='object', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='rec', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Subscript(
                                                                    value=Name(id='datas', ctx=Load()),
                                                                    slice=Constant(value='res_model', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='datas', ctx=Load()),
                                                                slice=Constant(value='res_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='func', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='getattr', ctx=Load()),
                                                        args=[
                                                            Name(id='rec', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='b', ctx=Load()),
                                                                slice=Constant(value='name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=None, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='func', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='error',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value="The %s model doesn't have a %s attribute!", kind=None),
                                                                    Subscript(
                                                                        value=Name(id='datas', ctx=Load()),
                                                                        slice=Constant(value='res_model', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Name(id='b', ctx=Load()),
                                                                        slice=Constant(value='name', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Continue(),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='func', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Break(),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='in the "%s" form, the "%s" button has unknown type %s', kind=None),
                                                            Name(id='action_name', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='b', ctx=Load()),
                                                                slice=Constant(value='string', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='b', ctx=Load()),
                                                                slice=Constant(value='type', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='ir.actions.report', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='window', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='datas', ctx=Load())],
                                            ),
                                            body=[
                                                Delete(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='datas', ctx=Load()),
                                                            slice=Constant(value='window', kind=None),
                                                            ctx=Del(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='datas', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='datas', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='action', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='datas', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='datas', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='datas', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='action', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='data', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='datas', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datas', ctx=Load()),
                                                    attr='copy',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='ids', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datas', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='ids', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Constant(value='ids', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='datas', ctx=Load())],
                                            ),
                                            body=[
                                                Delete(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='datas', ctx=Load()),
                                                            slice=Constant(value='ids', kind=None),
                                                            ctx=Del(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=Call(
                                                func=Name(id='try_report', ctx=Load()),
                                                args=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='uid', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='action', ctx=Load()),
                                                        slice=Constant(value='report_name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='ids', ctx=Load()),
                                                    Name(id='datas', ctx=Load()),
                                                    Name(id='context', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='our_module',
                                                        value=Name(id='our_module', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Name(id='res', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Cannot handle action of type %s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='act_model', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='log_test', ctx=Load()),
                        args=[
                            Constant(value='will be using %s action %s #%d', kind=None),
                            Name(id='act_model', ctx=Load()),
                            Name(id='act_xmlid', ctx=Load()),
                            Name(id='act_id', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='action', ctx=Store())],
                    value=Subscript(
                        value=Call(
                            func=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Name(id='env', ctx=Load()),
                                            slice=Name(id='act_model', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='act_id', ctx=Load())],
                                    keywords=[],
                                ),
                                attr='read',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        slice=Constant(value=0, kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assert(
                    test=Name(id='action', ctx=Load()),
                    msg=BinOp(
                        left=Constant(value='Could not read action %s[%s]', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Name(id='act_model', ctx=Load()),
                                Name(id='act_id', ctx=Load()),
                            ],
                            ctx=Load(),
                        ),
                    ),
                ),
                Assign(
                    targets=[Name(id='loop', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                While(
                    test=Name(id='action', ctx=Load()),
                    body=[
                        AugAssign(
                            target=Name(id='loop', ctx=Store()),
                            op=Add(),
                            value=Constant(value=1, kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='loop', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Constant(value=100, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Passed %d loops, giving up', kind=None),
                                            Name(id='loop', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[Constant(value='Too many loops at action', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='log_test', ctx=Load()),
                                args=[
                                    Constant(value='it is an %s action at loop #%d', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='type', kind=None),
                                            Constant(value='unknown', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='loop', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='_exec_action', ctx=Load()),
                                args=[
                                    Name(id='action', ctx=Load()),
                                    Name(id='datas', ctx=Load()),
                                    Name(id='env', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='result', ctx=Load()),
                                        Name(id='dict', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[Break()],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='datas', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='result', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='datas', kind=None),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='datas', ctx=Load()),
                            body=[
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='datas', kind=None),
                                            ctx=Del(),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Name(id='result', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
