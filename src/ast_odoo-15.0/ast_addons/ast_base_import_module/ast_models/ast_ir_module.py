Module(
    body=[
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='lxml', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='tempfile', asname=None)],
        ),
        Import(
            names=[alias(name='zipfile', asname=None)],
        ),
        ImportFrom(
            module='os.path',
            names=[alias(name='join', asname='opj')],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules',
            names=[alias(name='load_information_from_description_file', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='convert_file', asname=None),
                alias(name='exception_to_unicode', asname=None),
            ],
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
        Assign(
            targets=[Name(id='MAX_FILE_SIZE', ctx=Store())],
            value=BinOp(
                left=BinOp(
                    left=Constant(value=100, kind=None),
                    op=Mult(),
                    right=Constant(value=1024, kind=None),
                ),
                op=Mult(),
                right=Constant(value=1024, kind=None),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='IrModule',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.module.module', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='imported', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Imported Module', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_latest_version',
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
                            targets=[Name(id='imported_modules', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='m', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='imported',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='latest_version',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='module', ctx=Store()),
                            iter=Name(id='imported_modules', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='module', ctx=Load()),
                                            attr='installed_version',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='module', ctx=Load()),
                                        attr='latest_version',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrModule', ctx=Load()),
                                            BinOp(
                                                left=Name(id='self', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='imported_modules', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_latest_version',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='name', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_import_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='known_mods', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='known_mods_names', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='m', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                value=Name(id='m', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='m', ctx=Store()),
                                        iter=Name(id='known_mods', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='installed_mods', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='m', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='m', ctx=Store()),
                                        iter=Name(id='known_mods', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='installed', kind=None)],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='terp', ctx=Store())],
                            value=Call(
                                func=Name(id='load_information_from_description_file', ctx=Load()),
                                args=[Name(id='module', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='mod_path',
                                        value=Name(id='path', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='terp', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_values_from_terp',
                                    ctx=Load(),
                                ),
                                args=[Name(id='terp', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='version', kind=None),
                                ops=[In()],
                                comparators=[Name(id='terp', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='latest_version', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='terp', ctx=Load()),
                                        slice=Constant(value='version', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='unmet_dependencies', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='terp', ctx=Load()),
                                                slice=Constant(value='depends', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='difference',
                                    ctx=Load(),
                                ),
                                args=[Name(id='installed_mods', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='unmet_dependencies', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='unmet_dependencies', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[Constant(value='web_studio', kind=None)],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='_is_studio_custom', ctx=Load()),
                                                args=[Name(id='path', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='err', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Studio customizations require Studio', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='err', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Unmet module dependencies: \n\n - %s', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Constant(value='\n - ', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='known_mods', ctx=Load()),
                                                                        attr='filtered',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Lambda(
                                                                            args=arguments(
                                                                                posonlyargs=[],
                                                                                args=[arg(arg='mod', annotation=None, type_comment=None)],
                                                                                vararg=None,
                                                                                kwonlyargs=[],
                                                                                kw_defaults=[],
                                                                                kwarg=None,
                                                                                defaults=[],
                                                                            ),
                                                                            body=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='mod', ctx=Load()),
                                                                                    attr='name',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[In()],
                                                                                comparators=[Name(id='unmet_dependencies', ctx=Load())],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='shortdesc', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[Name(id='err', ctx=Load())],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='web_studio', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='installed_mods', ctx=Load())],
                                            ),
                                            Call(
                                                func=Name(id='_is_studio_custom', ctx=Load()),
                                                args=[Name(id='path', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Studio customizations require the Odoo Studio app.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='mod', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='known_mods_names', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='module', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='mod', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mod', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='state',
                                                        value=Constant(value='installed', kind=None),
                                                    ),
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='values', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='mode', ctx=Store())],
                                    value=IfExp(
                                        test=UnaryOp(
                                            op=Not(),
                                            operand=Name(id='force', ctx=Load()),
                                        ),
                                        body=Constant(value='update', kind=None),
                                        orelse=Constant(value='init', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assert(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='terp', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='installable', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    msg=Constant(value='Module not installable', kind=None),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='name',
                                                        value=Name(id='module', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='state',
                                                        value=Constant(value='installed', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='imported',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='values', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='mode', ctx=Store())],
                                    value=Constant(value='init', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        For(
                            target=Name(id='kind', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='data', kind=None),
                                    Constant(value='init_xml', kind=None),
                                    Constant(value='update_xml', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                For(
                                    target=Name(id='filename', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='terp', ctx=Load()),
                                        slice=Name(id='kind', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='ext', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='os', ctx=Load()),
                                                                    attr='path',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='splitext',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='filename', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='ext', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='.xml', kind=None),
                                                            Constant(value='.csv', kind=None),
                                                            Constant(value='.sql', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                                                            Constant(value='module %s: skip unsupported file %s', kind=None),
                                                            Name(id='module', ctx=Load()),
                                                            Name(id='filename', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='module %s: loading %s', kind=None),
                                                    Name(id='module', ctx=Load()),
                                                    Name(id='filename', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='noupdate', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='ext', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='.csv', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='kind', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='init', kind=None),
                                                                    Constant(value='init_xml', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='noupdate', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='pathname', ctx=Store())],
                                            value=Call(
                                                func=Name(id='opj', ctx=Load()),
                                                args=[
                                                    Name(id='path', ctx=Load()),
                                                    Name(id='filename', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='idref', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='convert_file', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='module', ctx=Load()),
                                                    Name(id='filename', ctx=Load()),
                                                    Name(id='idref', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='mode',
                                                        value=Name(id='mode', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='noupdate',
                                                        value=Name(id='noupdate', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='kind',
                                                        value=Name(id='kind', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='pathname',
                                                        value=Name(id='pathname', ctx=Load()),
                                                    ),
                                                ],
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
                            targets=[Name(id='path_static', ctx=Store())],
                            value=Call(
                                func=Name(id='opj', ctx=Load()),
                                args=[
                                    Name(id='path', ctx=Load()),
                                    Constant(value='static', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='IrAttachment', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.attachment', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='isdir',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path_static', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='root', ctx=Store()),
                                            Name(id='dirs', ctx=Store()),
                                            Name(id='files', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='walk',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path_static', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='static_file', ctx=Store()),
                                            iter=Name(id='files', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='full_path', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='opj', ctx=Load()),
                                                        args=[
                                                            Name(id='root', ctx=Load()),
                                                            Name(id='static_file', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                With(
                                                    items=[
                                                        withitem(
                                                            context_expr=Call(
                                                                func=Name(id='open', ctx=Load()),
                                                                args=[
                                                                    Name(id='full_path', ctx=Load()),
                                                                    Constant(value='rb', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            optional_vars=Name(id='fp', ctx=Store()),
                                                        ),
                                                    ],
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='data', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='base64', ctx=Load()),
                                                                    attr='b64encode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='fp', ctx=Load()),
                                                                            attr='read',
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
                                                    ],
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='url_path', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value='/{}{}', kind=None),
                                                            attr='format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='module', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='full_path', ctx=Load()),
                                                                                attr='split',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='path', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        slice=Constant(value=1, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='os', ctx=Load()),
                                                                            attr='path',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='sep',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='/', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
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
                                                                Name(id='url_path', ctx=Load()),
                                                                Name(id='str', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='url_path', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='url_path', ctx=Load()),
                                                                    attr='decode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='sys', ctx=Load()),
                                                                            attr='getfilesystemencoding',
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
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='filename', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='os', ctx=Load()),
                                                                    attr='path',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='url_path', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='values', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='name',
                                                                value=Name(id='filename', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='url',
                                                                value=Name(id='url_path', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='res_model',
                                                                value=Constant(value='ir.ui.view', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='type',
                                                                value=Constant(value='binary', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='datas',
                                                                value=Name(id='data', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='attachment', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='IrAttachment', ctx=Load()),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='url', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Name(id='url_path', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='type', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value='binary', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='res_model', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value='ir.ui.view', kind=None),
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
                                                If(
                                                    test=Name(id='attachment', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='attachment', ctx=Load()),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='values', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='IrAttachment', ctx=Load()),
                                                                    attr='create',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='values', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                FunctionDef(
                    name='import_zipfile',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module_file', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='module_file', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='No file sent.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='zipfile', ctx=Load()),
                                        attr='is_zipfile',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='module_file', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Only zip files are supported.', kind=None)],
                                                keywords=[],
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
                            targets=[Name(id='success', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='errors', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='module_names', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='zipfile', ctx=Load()),
                                            attr='ZipFile',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='module_file', ctx=Load()),
                                            Constant(value='r', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='z', ctx=Store()),
                                ),
                            ],
                            body=[
                                For(
                                    target=Name(id='zf', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='z', ctx=Load()),
                                        attr='filelist',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='zf', ctx=Load()),
                                                    attr='file_size',
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[Name(id='MAX_FILE_SIZE', ctx=Load())],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value="File '%s' exceed maximum allowed file size", kind=None),
                                                                    Attribute(
                                                                        value=Name(id='zf', ctx=Load()),
                                                                        attr='filename',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='tempfile', ctx=Load()),
                                                    attr='TemporaryDirectory',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='module_dir', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Import(
                                            names=[alias(name='odoo.modules.module', asname='module')],
                                        ),
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='odoo', ctx=Load()),
                                                                    attr='addons',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='__path__',
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='module_dir', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='z', ctx=Load()),
                                                            attr='extractall',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='module_dir', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='dirs', ctx=Store())],
                                                    value=ListComp(
                                                        elt=Name(id='d', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='d', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='os', ctx=Load()),
                                                                        attr='listdir',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='module_dir', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='os', ctx=Load()),
                                                                                attr='path',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='isdir',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='opj', ctx=Load()),
                                                                                args=[
                                                                                    Name(id='module_dir', ctx=Load()),
                                                                                    Name(id='d', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='mod_name', ctx=Store()),
                                                    iter=Name(id='dirs', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='module_names', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='mod_name', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Try(
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='path', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='opj', ctx=Load()),
                                                                        args=[
                                                                            Name(id='module_dir', ctx=Load()),
                                                                            Name(id='mod_name', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_import_module',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='mod_name', ctx=Load()),
                                                                            Name(id='path', ctx=Load()),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='force',
                                                                                value=Name(id='force', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='success', ctx=Load()),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='mod_name', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
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
                                                                                    attr='exception',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='Error while importing module', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='errors', ctx=Load()),
                                                                                    slice=Name(id='mod_name', ctx=Load()),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Name(id='exception_to_unicode', ctx=Load()),
                                                                                args=[Name(id='e', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            finalbody=[],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[],
                                            orelse=[],
                                            finalbody=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='odoo', ctx=Load()),
                                                                    attr='addons',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='__path__',
                                                                ctx=Load(),
                                                            ),
                                                            attr='remove',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='module_dir', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=ListComp(
                                elt=BinOp(
                                    left=Constant(value="Successfully imported module '%s'", kind=None),
                                    op=Mod(),
                                    right=Name(id='mod', ctx=Load()),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='mod', ctx=Store()),
                                        iter=Name(id='success', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='mod', ctx=Store()),
                                    Name(id='error', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='errors', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value="Error while importing module '%s'.\n\n %s \n Make sure those modules are installed and try again.", kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='mod', ctx=Load()),
                                                        Name(id='error', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='\n', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='r', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='module_names', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='module_uninstall',
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
                            targets=[Name(id='modules_to_delete', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='imported', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='module_uninstall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='modules_to_delete', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='deleting imported modules upon uninstallation: %s', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value=', ', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='modules_to_delete', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='name', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='modules_to_delete', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='_is_studio_custom',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='path', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Checks the to-be-imported records to see if there are any references to\n    studio, which would mean that the module was created using studio\n\n    Returns True if any of the records contains a context with the key\n    studio in it, False if none of the records do\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='filepaths', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='level', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='os', ctx=Load()),
                            attr='walk',
                            ctx=Load(),
                        ),
                        args=[Name(id='path', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        AugAssign(
                            target=Name(id='filepaths', ctx=Store()),
                            op=Add(),
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Subscript(
                                            value=Name(id='level', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        Name(id='fn', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='fn', ctx=Store()),
                                        iter=Subscript(
                                            value=Name(id='level', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='filepaths', ctx=Store())],
                    value=ListComp(
                        elt=Name(id='fp', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Name(id='fp', ctx=Store()),
                                iter=Name(id='filepaths', ctx=Load()),
                                ifs=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fp', ctx=Load()),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='endswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.xml', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                is_async=0,
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='fp', ctx=Store()),
                    iter=Name(id='filepaths', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='root', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='lxml', ctx=Load()),
                                                attr='etree',
                                                ctx=Load(),
                                            ),
                                            attr='parse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='fp', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='getroot',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='root', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='ctx', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ast', ctx=Load()),
                                                    attr='literal_eval',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='context', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='ctx', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='ctx', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='studio', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[],
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Constant(value=False, kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
