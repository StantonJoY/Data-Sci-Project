Module(
    body=[
        Expr(
            value=Constant(value='\nThis code is what let us use ES6-style modules in odoo.\nClassic Odoo modules are composed of a top-level :samp:`odoo.define({name},{body_function})` call.\nThis processor will take files starting with an `@odoo-module` annotation (in a comment) and convert them to classic modules.\nIf any file has the /** odoo-module */ on top of it, it will get processed by this class.\nIt performs several operations to get from ES6 syntax to the usual odoo one with minimal changes.\nThis is done on the fly, this not a pre-processing tool.\n\nCaveat: This is done without a full parser, only using regex. One can only expect to cover as much edge cases\nas possible with reasonable limitations. Also, this only changes imports and exports, so all JS features used in\nthe original source need to be supported by the browsers.\n', kind=None),
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='partial', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='transpile_javascript',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='url', annotation=None, type_comment=None),
                    arg(arg='content', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile the code from native JS modules to custom odoo modules.\n\n    :param content: The original source code\n    :param url: The url of the file in the project\n    :return: The transpiled source code\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='module_path', ctx=Store())],
                    value=Call(
                        func=Name(id='url_to_module_path', ctx=Load()),
                        args=[Name(id='url', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='legacy_odoo_define', ctx=Store())],
                    value=Call(
                        func=Name(id='get_aliased_odoo_define_content', ctx=Load()),
                        args=[
                            Name(id='module_path', ctx=Load()),
                            Name(id='content', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='steps', ctx=Store())],
                    value=List(
                        elts=[
                            Name(id='convert_legacy_default_import', ctx=Load()),
                            Name(id='convert_basic_import', ctx=Load()),
                            Name(id='convert_default_import', ctx=Load()),
                            Name(id='convert_star_import', ctx=Load()),
                            Name(id='convert_unnamed_relative_import', ctx=Load()),
                            Name(id='convert_from_export', ctx=Load()),
                            Name(id='convert_star_from_export', ctx=Load()),
                            Call(
                                func=Name(id='partial', ctx=Load()),
                                args=[
                                    Name(id='convert_relative_require', ctx=Load()),
                                    Name(id='url', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            Name(id='remove_index', ctx=Load()),
                            Name(id='convert_export_function_or_class', ctx=Load()),
                            Name(id='convert_variable_export', ctx=Load()),
                            Name(id='convert_object_export', ctx=Load()),
                            Name(id='convert_default_export', ctx=Load()),
                            Call(
                                func=Name(id='partial', ctx=Load()),
                                args=[
                                    Name(id='wrap_with_odoo_define', ctx=Load()),
                                    Name(id='module_path', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='s', ctx=Store()),
                    iter=Name(id='steps', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Name(id='s', ctx=Load()),
                                args=[Name(id='content', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                If(
                    test=Name(id='legacy_odoo_define', ctx=Load()),
                    body=[
                        AugAssign(
                            target=Name(id='content', ctx=Store()),
                            op=Add(),
                            value=Name(id='legacy_odoo_define', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='content', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='URL_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    /?(?P<module>\\S+)    # /module name\n    /([\\S/]*/)?static/   # ... /static/\n    (?P<type>src|tests|lib)  # src, test, or lib file\n    (?P<url>/[\\S/]*)     # URL (/...)\n    ', kind=None),
                    Attribute(
                        value=Name(id='re', ctx=Load()),
                        attr='VERBOSE',
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='url_to_module_path',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='url', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Odoo modules each have a name. (odoo.define("<the name>", async function (require) {...});\n    It is used in to be required later. (const { something } = require("<the name>").\n    The transpiler transforms the url of the file in the project to this name.\n    It takes the module name and add a @ on the start of it, and map it to be the source of the static/src (or\n    static/tests, or static/lib) folder in that module.\n\n    in: web/static/src/one/two/three.js\n    out: @web/one/two/three.js\n    The module would therefore be defined and required by this path.\n\n    :param url: an url in the project\n    :return: a special path starting with @<module-name>.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='match', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='URL_RE', ctx=Load()),
                            attr='match',
                            ctx=Load(),
                        ),
                        args=[Name(id='url', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='match', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Subscript(
                                value=Name(id='match', ctx=Load()),
                                slice=Constant(value='url', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='url', ctx=Load()),
                                    attr='endswith',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='/index.js', kind=None),
                                            Constant(value='/index', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='url', ctx=Store()),
                                                Name(id='_', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='url', ctx=Load()),
                                            attr='rsplit',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/', kind=None),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='url', ctx=Load()),
                                    attr='endswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='.js', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='url', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='url', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=3, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='match', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='src', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Constant(value='@%s%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='match', ctx=Load()),
                                                    slice=Constant(value='module', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Name(id='url', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='match', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='lib', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Constant(value='@%s/../lib%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='match', ctx=Load()),
                                                            slice=Constant(value='module', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='url', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=BinOp(
                                                left=Constant(value='@%s/../tests%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='match', ctx=Load()),
                                                            slice=Constant(value='module', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='url', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    orelse=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value="The js file %r must be in the folder '/static/src' or '/static/lib' or '/static/test'", kind=None),
                                        op=Mod(),
                                        right=Name(id='url', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='wrap_with_odoo_define',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='module_path', annotation=None, type_comment=None),
                    arg(arg='content', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Wraps the current content (source code) with the odoo.define call.\n    Should logically be called once all other operations have been performed.\n    ', kind=None),
                ),
                Return(
                    value=JoinedStr(
                        values=[
                            Constant(value='odoo.define(', kind=None),
                            FormattedValue(
                                value=Name(id='module_path', ctx=Load()),
                                conversion=114,
                                format_spec=None,
                            ),
                            Constant(value=", async function (require) {\n'use strict';\nlet __exports = {};\n", kind=None),
                            FormattedValue(
                                value=Name(id='content', ctx=Load()),
                                conversion=-1,
                                format_spec=None,
                            ),
                            Constant(value='\nreturn __exports;\n});\n', kind=None),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='EXPORT_FCT_OR_CLASS_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^\n    (?P<space>\\s*)                          # space and empty line\n    export\\s+                               # export\n    (?P<type>(async\\s+)?function|class)\\s+  # async function or function or class\n    (?P<identifier>\\w+)                     # name of the class or the function\n    ', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_export_function_or_class',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile functions and classes that are being exported.\n\n    .. code-block:: javascript\n\n        // before\n        export function name\n        // after\n        const name = __exports.name = function name\n\n        // before\n        export async function name\n        // after\n        const name = __exports.name = async function name\n\n        // before\n        export class name\n        // after\n        const name = __exports.name = class name\n\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='repl', ctx=Store())],
                    value=Constant(value='\\g<space>const \\g<identifier> = __exports.\\g<identifier> = \\g<type> \\g<identifier>', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='EXPORT_FCT_OR_CLASS_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='EXPORT_FCT_OR_CLASS_DEFAULT_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^\n    (?P<space>\\s*)                          # space and empty line\n    export\\s+default\\s+                     # export default\n    (?P<type>(async\\s+)?function|class)\\s+  # async function or function or class\n    (?P<identifier>\\w+)                     # name of the class or the function\n    ', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_export_function_or_class_default',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile functions and classes that are being exported as default value.\n\n    .. code-block:: javascript\n\n        // before\n        export default function name\n        // after\n        const name = __exports[Symbol.for("default")] = function name\n\n        // before\n        export default async function name\n        // after\n        const name = __exports[Symbol.for("default")] = async function name\n\n        // before\n        export default class name\n        // after\n        const name = __exports[Symbol.for("default")] = class name\n\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='repl', ctx=Store())],
                    value=Constant(value='\\g<space>const \\g<identifier> = __exports[Symbol.for("default")] = \\g<type> \\g<identifier>', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='EXPORT_FCT_OR_CLASS_DEFAULT_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='EXPORT_VAR_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^\n    (?P<space>\\s*)              # space and empty line\n    export\\s+                   # export\n    (?P<type>let|const|var)\\s+  # let or cont or var\n    (?P<identifier>\\w+)         # variable name\n    ', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_variable_export',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile variables that are being exported.\n\n    .. code-block:: javascript\n\n        // before\n        export let name\n        // after\n        let name = __exports.name\n        // (same with var and const)\n\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='repl', ctx=Store())],
                    value=Constant(value='\\g<space>\\g<type> \\g<identifier> = __exports.\\g<identifier>', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='EXPORT_VAR_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='EXPORT_DEFAULT_VAR_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^\n    (?P<space>\\s*)              # space and empty line\n    export\\s+default\\s+         # export default\n    (?P<type>let|const|var)\\s+  # let or const or var\n    (?P<identifier>\\w+)\\s*      # variable name\n    ', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_variable_export_default',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile the variables that are exported as default values.\n\n    .. code-block:: javascript\n\n        // before\n        export default let name\n        // after\n        let name = __exports[Symbol.for("default")]\n\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='repl', ctx=Store())],
                    value=Constant(value='\\g<space>\\g<type> \\g<identifier> = __exports[Symbol.for("default")]', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='EXPORT_DEFAULT_VAR_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='EXPORT_OBJECT_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^\n    (?P<space>\\s*)                      # space and empty line\n    export\\s*                           # export\n    (?P<object>{[\\w\\s,]+})              # { a, b, c as x, ... }\n    ', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_object_export',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile exports of multiple elements\n\n    .. code-block:: javascript\n\n        // before\n        export { a, b, c as x }\n        // after\n        Object.assign(__exports, { a, b, x: c })\n    ', kind=None),
                ),
                FunctionDef(
                    name='repl',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='matchobj', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='object_process', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value='{', kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Constant(value=', ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Call(
                                                    func=Name(id='convert_as', ctx=Load()),
                                                    args=[Name(id='val', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='val', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='matchobj', ctx=Load()),
                                                                        slice=Constant(value='object', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Slice(
                                                                        lower=Constant(value=1, kind=None),
                                                                        upper=UnaryOp(
                                                                            op=USub(),
                                                                            operand=Constant(value=1, kind=None),
                                                                        ),
                                                                        step=None,
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=',', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value='}', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='space', ctx=Store())],
                            value=Subscript(
                                value=Name(id='matchobj', ctx=Load()),
                                slice=Constant(value='space', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=JoinedStr(
                                values=[
                                    FormattedValue(
                                        value=Name(id='space', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value='Object.assign(__exports, ', kind=None),
                                    FormattedValue(
                                        value=Name(id='object_process', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=')', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='EXPORT_OBJECT_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='EXPORT_FROM_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^\n    (?P<space>\\s*)                      # space and empty line\n    export\\s*                           # export\n    (?P<object>{[\\w\\s,]+})\\s*           # { a, b, c as x, ... }\n    from\\s*                             # from\n    (?P<path>(?P<quote>["\'`])([^"\'`]+)(?P=quote))   # "file path" ("some/path.js")\n    ', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_from_export',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile exports coming from another source\n\n    .. code-block:: javascript\n\n        // before\n        export { a, b, c as x } from "some/path.js"\n        // after\n        { a, b, c } = {require("some/path.js"); Object.assign(__exports, { a, b, x: c });}\n    ', kind=None),
                ),
                FunctionDef(
                    name='repl',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='matchobj', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='object_clean', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value='{', kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Constant(value=',', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Call(
                                                    func=Name(id='remove_as', ctx=Load()),
                                                    args=[Name(id='val', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='val', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='matchobj', ctx=Load()),
                                                                        slice=Constant(value='object', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Slice(
                                                                        lower=Constant(value=1, kind=None),
                                                                        upper=UnaryOp(
                                                                            op=USub(),
                                                                            operand=Constant(value=1, kind=None),
                                                                        ),
                                                                        step=None,
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=',', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value='}', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='object_process', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value='{', kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Constant(value=', ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Call(
                                                    func=Name(id='convert_as', ctx=Load()),
                                                    args=[Name(id='val', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='val', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='matchobj', ctx=Load()),
                                                                        slice=Constant(value='object', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Slice(
                                                                        lower=Constant(value=1, kind=None),
                                                                        upper=UnaryOp(
                                                                            op=USub(),
                                                                            operand=Constant(value=1, kind=None),
                                                                        ),
                                                                        step=None,
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value=',', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value='}', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='%(space)s{const %(object_clean)s = require(%(path)s);Object.assign(__exports, %(object_process)s)}', kind=None),
                                op=Mod(),
                                right=Dict(
                                    keys=[
                                        Constant(value='object_clean', kind=None),
                                        Constant(value='object_process', kind=None),
                                        Constant(value='space', kind=None),
                                        Constant(value='path', kind=None),
                                    ],
                                    values=[
                                        Name(id='object_clean', ctx=Load()),
                                        Name(id='object_process', ctx=Load()),
                                        Subscript(
                                            value=Name(id='matchobj', ctx=Load()),
                                            slice=Constant(value='space', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='matchobj', ctx=Load()),
                                            slice=Constant(value='path', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='EXPORT_FROM_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='EXPORT_STAR_FROM_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^\n    (?P<space>\\s*)                      # space and empty line\n    export\\s*\\*\\s*from\\s*               # export * from\n    (?P<path>(?P<quote>["\'`])([^"\'`]+)(?P=quote))   # "file path" ("some/path.js")\n    ', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_star_from_export',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile exports star coming from another source\n\n    .. code-block:: javascript\n\n        // before\n        export * from "some/path.js"\n        // after\n        Object.assign(__exports, require("some/path.js"))\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='repl', ctx=Store())],
                    value=Constant(value='\\g<space>Object.assign(__exports, require(\\g<path>))', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='EXPORT_STAR_FROM_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='EXPORT_DEFAULT_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^\n    (?P<space>\\s*)      # space and empty line\n    export\\s+default    # export default\n    (\\s+\\w+\\s*=)?       # something (optional)\n    ', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_default_export',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    This function handles the default exports.\n    Either by calling another operation with a TRUE flag, and if any default is left, doing a simple replacement.\n\n    (see convert_export_function_or_class_default and convert_variable_export_default).\n    +\n    .. code-block:: javascript\n\n        // before\n        export default\n        // after\n        __exports[Symbol.for("default")] =\n\n    .. code-block:: javascript\n\n        // before\n        export default something =\n        // after\n        __exports[Symbol.for("default")] =\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='new_content', ctx=Store())],
                    value=Call(
                        func=Name(id='convert_export_function_or_class_default', ctx=Load()),
                        args=[Name(id='content', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_content', ctx=Store())],
                    value=Call(
                        func=Name(id='convert_variable_export_default', ctx=Load()),
                        args=[Name(id='new_content', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='repl', ctx=Store())],
                    value=Constant(value='\\g<space>__exports[Symbol.for("default")] =', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='EXPORT_DEFAULT_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='new_content', ctx=Load()),
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
            targets=[Name(id='IMPORT_BASIC_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^\n    (?P<space>\\s*)                      # space and empty line\n    import\\s+                           # import\n    (?P<object>{(\\s*\\w+\\s*,?\\s*)+})\\s*  # { a, b, c as x, ... }\n    from\\s*                             # from\n    (?P<path>(?P<quote>["\'`])([^"\'`]+)(?P=quote))   # "file path" ("some/path")\n    ', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_basic_import',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile the simpler import call.\n\n    .. code-block:: javascript\n\n        // before\n        import { a, b, c as x } from "some/path"\n        // after\n        const {a, b, c: x} = require("some/path")\n    ', kind=None),
                ),
                FunctionDef(
                    name='repl',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='matchobj', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='new_object', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='matchobj', ctx=Load()),
                                        slice=Constant(value='object', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=' as ', kind=None),
                                    Constant(value=': ', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=JoinedStr(
                                values=[
                                    FormattedValue(
                                        value=Subscript(
                                            value=Name(id='matchobj', ctx=Load()),
                                            slice=Constant(value='space', kind=None),
                                            ctx=Load(),
                                        ),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value='const ', kind=None),
                                    FormattedValue(
                                        value=Name(id='new_object', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' = require(', kind=None),
                                    FormattedValue(
                                        value=Subscript(
                                            value=Name(id='matchobj', ctx=Load()),
                                            slice=Constant(value='path', kind=None),
                                            ctx=Load(),
                                        ),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=')', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='IMPORT_BASIC_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='IMPORT_LEGACY_DEFAULT_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^\n    (?P<space>\\s*)                                      # space and empty line\n    import\\s+                                           # import\n    (?P<identifier>\\w+)\\s*                              # default variable name\n    from\\s*                                             # from\n    (?P<path>(?P<quote>["\'`])([^@\\."\'`][^"\'`]*)(?P=quote))  # legacy alias file ("addon_name.module_name" or "some/path")\n    ', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_legacy_default_import',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile legacy imports (that were used as they were default import).\n    Legacy imports means that their name is not a path but a <addon_name>.<module_name>.\n    It requires slightly different processing.\n\n    .. code-block:: javascript\n\n        // before\n        import module_name from "addon.module_name"\n        // after\n        const module_name = require("addon.module_name")\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='repl', ctx=Store())],
                    value=Constant(value='\\g<space>const \\g<identifier> = require(\\g<path>)', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='IMPORT_LEGACY_DEFAULT_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='IMPORT_DEFAULT', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^\n    (?P<space>\\s*)                      # space and empty line\n    import\\s+                           # import\n    (?P<identifier>\\w+)\\s*              # default variable name\n    from\\s*                             # from\n    (?P<path>(?P<quote>["\'`])([^"\'`]+)(?P=quote))   # "file path" ("some/path")\n    ', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_default_import',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile the default import call.\n\n    .. code-block:: javascript\n\n        // before\n        import something from "some/path"\n        // after\n        const something = require("some/path")[Symbol.for("default")]\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='repl', ctx=Store())],
                    value=Constant(value='\\g<space>const \\g<identifier> = require(\\g<path>)[Symbol.for("default")]', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='IMPORT_DEFAULT', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='RELATIVE_REQUIRE_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    require\\((?P<quote>["\'`])([^@"\'`]+)(?P=quote)\\)  # require("some/path")\n    ', kind=None),
                    Attribute(
                        value=Name(id='re', ctx=Load()),
                        attr='VERBOSE',
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_relative_require',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='url', annotation=None, type_comment=None),
                    arg(arg='content', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Convert the relative path contained in a \'require()\'\n    to the new path system (@module/path)\n    .. code-block:: javascript\n\n        // Relative path:\n        // before\n        require("./path")\n        // after\n        require("@module/path")\n\n        // Not a relative path:\n        // before\n        require("other_alias")\n        // after\n        require("other_alias")\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='new_content', ctx=Store())],
                    value=Name(id='content', ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='quote', ctx=Store()),
                            Name(id='path', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='RELATIVE_REQUIRE_RE', ctx=Load()),
                            attr='findall',
                            ctx=Load(),
                        ),
                        args=[Name(id='new_content', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='path', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Constant(value='/', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='path', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='pattern', ctx=Store())],
                                    value=JoinedStr(
                                        values=[
                                            Constant(value='require\\(', kind=None),
                                            FormattedValue(
                                                value=Name(id='quote', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            FormattedValue(
                                                value=Name(id='path', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            FormattedValue(
                                                value=Name(id='quote', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='\\)', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='repl', ctx=Store())],
                                    value=JoinedStr(
                                        values=[
                                            Constant(value='require("', kind=None),
                                            FormattedValue(
                                                value=Call(
                                                    func=Name(id='relative_path_to_module_path', ctx=Load()),
                                                    args=[
                                                        Name(id='url', ctx=Load()),
                                                        Name(id='path', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='")', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='pattern', ctx=Load()),
                                            Name(id='repl', ctx=Load()),
                                            Name(id='new_content', ctx=Load()),
                                        ],
                                        keywords=[],
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
                Return(
                    value=Name(id='new_content', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='IMPORT_STAR', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^(?P<space>\\s*)       # indentation\n    import\\s+\\*\\s+as\\s+   # import * as\n    (?P<identifier>\\w+)   # alias\n    \\s*from\\s*            # from\n    (?P<path>[^;\\n]+)     # path\n', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_star_import',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile import star.\n\n    .. code-block:: javascript\n\n        // before\n        import * as name from "some/path"\n        // after\n        const name = require("some/path")\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='repl', ctx=Store())],
                    value=Constant(value='\\g<space>const \\g<identifier> = require(\\g<path>)', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='IMPORT_STAR', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='IMPORT_UNNAMED_RELATIVE_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    ^(?P<space>\\s*)     # indentation\n    import\\s+           # import\n    (?P<path>[^;\\n]+)   # relative path\n', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='convert_unnamed_relative_import',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Transpile relative "direct" imports. Direct meaning they are not store in a variable.\n\n    .. code-block:: javascript\n\n        // before\n        import "some/path"\n        // after\n        require("some/path")\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='repl', ctx=Store())],
                    value=Constant(value='require(\\g<path>)', kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='IMPORT_UNNAMED_RELATIVE_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            targets=[Name(id='URL_INDEX_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    require\\s*                 # require\n    \\(\\s*                      # (\n    (?P<path>(?P<quote>["\'`])([^"\'`]*/index/?)(?P=quote))  # path ended by /index or /index/\n    \\s*\\)                      # )\n', kind=None),
                    BinOp(
                        left=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='MULTILINE',
                            ctx=Load(),
                        ),
                        op=BitOr(),
                        right=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='VERBOSE',
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='remove_index',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Remove in the paths the /index.js.\n    We want to be able to import a module just trough its directory name if it contains an index.js.\n    So we no longer need to specify the index.js in the paths.\n    ', kind=None),
                ),
                FunctionDef(
                    name='repl',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='matchobj', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Subscript(
                                value=Name(id='matchobj', ctx=Load()),
                                slice=Constant(value='path', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_path', ctx=Store())],
                            value=BinOp(
                                left=Subscript(
                                    value=Name(id='path', ctx=Load()),
                                    slice=Slice(
                                        lower=None,
                                        upper=Call(
                                            func=Attribute(
                                                value=Name(id='path', ctx=Load()),
                                                attr='rfind',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='/index', kind=None)],
                                            keywords=[],
                                        ),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Subscript(
                                    value=Name(id='path', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=JoinedStr(
                                values=[
                                    Constant(value='require(', kind=None),
                                    FormattedValue(
                                        value=Name(id='new_path', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=')', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='URL_INDEX_RE', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='repl', ctx=Load()),
                            Name(id='content', ctx=Load()),
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
            name='relative_path_to_module_path',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='url', annotation=None, type_comment=None),
                    arg(arg='path_rel', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Convert the relative path into a module path, which is more generic and fancy.\n\n    :param path_rel: a relative path to the current url.\n    :return: module path (@module/...)\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='url_split', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='url', ctx=Load()),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='/', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='path_rel_split', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='path_rel', ctx=Load()),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='/', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='nb_back', ctx=Store())],
                    value=BinOp(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[
                                ListComp(
                                    elt=Name(id='v', ctx=Load()),
                                    generators=[
                                        comprehension(
                                            target=Name(id='v', ctx=Store()),
                                            iter=Name(id='path_rel_split', ctx=Load()),
                                            ifs=[
                                                Compare(
                                                    left=Name(id='v', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='..', kind=None)],
                                                ),
                                            ],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                            ],
                            keywords=[],
                        ),
                        op=Add(),
                        right=Constant(value=1, kind=None),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='/', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Subscript(
                                    value=Name(id='url_split', ctx=Load()),
                                    slice=Slice(
                                        lower=None,
                                        upper=UnaryOp(
                                            op=USub(),
                                            operand=Name(id='nb_back', ctx=Load()),
                                        ),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=ListComp(
                                    elt=Name(id='v', ctx=Load()),
                                    generators=[
                                        comprehension(
                                            target=Name(id='v', ctx=Store()),
                                            iter=Name(id='path_rel_split', ctx=Load()),
                                            ifs=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Compare(
                                                        left=Name(id='v', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='..', kind=None),
                                                                    Constant(value='.', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='url_to_module_path', ctx=Load()),
                        args=[Name(id='result', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='ODOO_MODULE_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='\n    \\s*                                       # some starting space\n    \\/(\\*|\\/).*\\s*                            # // or /*\n    @odoo-module                              # @odoo-module\n    (\\s+alias=(?P<alias>[\\w.]+))?             # alias=web.AbstractAction (optional)\n    (\\s+default=(?P<default>False|false|0))?  # default=False or false or 0 (optional)\n', kind=None),
                    Attribute(
                        value=Name(id='re', ctx=Load()),
                        attr='VERBOSE',
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='is_odoo_module',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='content', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Detect if the file is a native odoo module.\n    We look for a comment containing @odoo-module.\n\n    :param content: source code\n    :return: is this a odoo module that need transpilation ?\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='ODOO_MODULE_RE', ctx=Load()),
                            attr='match',
                            ctx=Load(),
                        ),
                        args=[Name(id='content', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='bool', ctx=Load()),
                        args=[Name(id='result', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_aliased_odoo_define_content',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='module_path', annotation=None, type_comment=None),
                    arg(arg='content', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    To allow smooth transition between the new system and the legacy one, we have the possibility to\n    defined an alternative module name (an alias) that will act as proxy between legacy require calls and\n    new modules.\n\n    Example:\n    If we have a require call somewhere in the odoo source base being:\n    > vat AbstractAction require("web.AbstractAction")\n    we have a problem when we will have converted to module to ES6: its new name will be more like\n    "web/chrome/abstract_action". So the require would fail !\n    So we add a second small modules, an alias, as such:\n    > odoo.define("web/chrome/abstract_action", async function(require) {\n    >  return require(\'web.AbstractAction\')[Symbol.for("default")];\n    > });\n\n    To generate this, change your comment on the top of the file.\n\n    .. code-block:: javascript\n\n        // before\n        /** @odoo-module */\n        // after\n        /** @odoo-module alias=web.AbstractAction */\n\n    Notice that often, the legacy system acted like they it did defaukt imports. That\'s why we have the\n    "[Symbol.for("default")];" bit. If your use case does not need this default import, just do:\n\n    .. code-block:: javascript\n\n        // before\n        /** @odoo-module */\n        // after\n        /** @odoo-module alias=web.AbstractAction default=false */\n\n    :return: the alias content to append to the source code.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='matchobj', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='ODOO_MODULE_RE', ctx=Load()),
                            attr='match',
                            ctx=Load(),
                        ),
                        args=[Name(id='content', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='matchobj', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='alias', ctx=Store())],
                            value=Subscript(
                                value=Name(id='matchobj', ctx=Load()),
                                slice=Constant(value='alias', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='alias', ctx=Load()),
                            body=[
                                If(
                                    test=Subscript(
                                        value=Name(id='matchobj', ctx=Load()),
                                        slice=Constant(value='default', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Constant(value="\nodoo.define(`%s`, async function(require) {\n                        return require('%s');\n                        });\n", kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='alias', ctx=Load()),
                                                        Name(id='module_path', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=BinOp(
                                                left=Constant(value='\nodoo.define(`%s`, async function(require) {\n                        return require(\'%s\')[Symbol.for("default")];\n                        });\n', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='alias', ctx=Load()),
                                                        Name(id='module_path', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='convert_as',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='val', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='parts', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='val', ctx=Load()),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value=' as ', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=IfExp(
                        test=Compare(
                            left=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='parts', ctx=Load())],
                                keywords=[],
                            ),
                            ops=[Lt()],
                            comparators=[Constant(value=2, kind=None)],
                        ),
                        body=Name(id='val', ctx=Load()),
                        orelse=BinOp(
                            left=Constant(value='%s: %s', kind=None),
                            op=Mod(),
                            right=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='reversed', ctx=Load()),
                                        args=[Name(id='parts', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='remove_as',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='val', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='parts', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='val', ctx=Load()),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value=' as ', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=IfExp(
                        test=Compare(
                            left=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='parts', ctx=Load())],
                                keywords=[],
                            ),
                            ops=[Lt()],
                            comparators=[Constant(value=2, kind=None)],
                        ),
                        body=Name(id='val', ctx=Load()),
                        orelse=Subscript(
                            value=Name(id='parts', ctx=Load()),
                            slice=Constant(value=0, kind=None),
                            ctx=Load(),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
